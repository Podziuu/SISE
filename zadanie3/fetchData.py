from ucimlrepo import fetch_ucirepo 
  
# fetch dataset 
mushroom = fetch_ucirepo(id=73) 
  
# data (as pandas dataframes) 
X = mushroom.data.features 
X.to_csv('zadanie3/data/features.csv')
y = mushroom.data.targets 
y.to_csv('zadanie3/data/targets.csv')
  
# metadata 
print(mushroom.metadata) 
  
# variable information 
variableInformation = mushroom.variables
print(variableInformation)
variableInformation.to_csv('zadanie3/data/variable_information.csv') 

