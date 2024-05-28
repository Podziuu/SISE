import pandas as pd
import numpy as np
import tensorflow_decision_forests as tfdf

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
test_set_size = int(len(data) * 0.30 ) #test ratio od uzytkownika brac
test_indices = shuffled_indices[:test_set_size]
train_indices = shuffled_indices[test_set_size:]
trainData = data.iloc[train_indices] 
testData =data.iloc[test_indices]

trainDs = tfdf.keras.pd_dataframe_to_tf_dataset(trainData, label='poisonous')
testDs = tfdf.keras.pd_dataframe_to_tf_dataset(testData, label='poisonous')

randomForest = tfdf.keras.RandomForestModel(verbose=2)

randomForest.fit(trainDs)

randomForest.compile(metrics=['accuracy'])
evaluation = randomForest.evaluate(testDs, return_dict=True)

for name, value in evaluation.items():
    print(f'{name}: {value}')
