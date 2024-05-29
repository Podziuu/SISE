import pandas as pd
import numpy as np
import tensorflow_decision_forests as tfdf
import tensorflow as tf
import argparse
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix

parser = argparse.ArgumentParser()
parser.add_argument('--testPercent', type=float, default=0.98)
parser.add_argument('--numTrees', type=int, default=300)
parser.add_argument('--maxDepth', type=int, default=16)
parser.add_argument('--minExamples', type=int, default=5)
parser.add_argument('--bootstrap', type=bool, default=True)
args = parser.parse_args()
print('\n\n\n\n\n\n')

X = pd.read_csv('zadanie3/data/features.csv', index_col=0)
Y = pd.read_csv('zadanie3/data/targets.csv', index_col=0) 

# pandaX = pd.DataFrame(X)
# pandaY = pd.DataFrame(Y)

# convert categorical labels to numeric
labels = Y['poisonous'].unique().tolist()
numericLabels = Y.map(labels.index)

data = pd.concat([X, numericLabels], axis=1)

# make test and train datasets
shuffled_indices = np.random.permutation(len(data))
test_set_size = int(len(data) * args.testPercent) #test ratio od uzytkownika brac
test_indices = shuffled_indices[:test_set_size]
train_indices = shuffled_indices[test_set_size:]
trainData = data.iloc[train_indices] 
testData =data.iloc[test_indices]

trainDs = tfdf.keras.pd_dataframe_to_tf_dataset(trainData, label='poisonous')
testDs = tfdf.keras.pd_dataframe_to_tf_dataset(testData, label='poisonous')

randomForest = tfdf.keras.RandomForestModel(num_trees=args.numTrees, 
                                            max_depth=args.maxDepth,
                                            min_examples=args.minExamples,
                                            bootstrap_training_dataset=args.bootstrap,
                                            growing_strategy='BEST_FIRST_GLOBAL',
                                            verbose=2)
randomForest.compile(metrics=['accuracy'])

randomForest.fit(trainDs)
print('Summary: \n \n \n')
# randomForest.summary()


print('Evaluation: \n \n \n')
evaluation = randomForest.evaluate(testDs, return_dict=True)

for name, value in evaluation.items():
    print(f'{name}: {value}')

logs = randomForest.make_inspector().training_logs()

plt.figure(figsize=(12, 6))

# Wykres dokładności w zależności od liczby drzew
plt.subplot(1, 2, 1)
plt.plot([log.num_trees for log in logs], [log.evaluation.accuracy for log in logs])
plt.xlabel("Liczba drzew")
plt.ylabel("Dokładność")
plt.title("Dokładność od liczby drzew")

# Wykres strat w zależności od liczby drzew
plt.subplot(1, 2, 2)
plt.plot([log.num_trees for log in logs], [log.evaluation.loss for log in logs])
plt.xlabel("Liczba drzew")
plt.ylabel("Strata logarytmiczna")
plt.title("Strata logarytmiczna od liczby drzew")


plt.savefig('training_accuracy.png')


predictions = randomForest.predict(testDs)
predicted_labels = (predictions > 0.5).astype(int)
true_labels = testData['poisonous']
matrix = confusion_matrix(true_labels, predicted_labels)
print('Confusion matrix: \n')
print(matrix)

precision = np.diag(matrix) / np.sum(matrix, axis=0)
recall = np.diag(matrix) / np.sum(matrix, axis=1)
f_measure = 2 * (precision * recall) / (precision + recall)

print("\nPrecyzja (Precision):", precision)
print("Czułość (Recall):", recall)
print("Miara F (F-measure):", f_measure)
# plt.show()


