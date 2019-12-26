#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 14:16:03 2018

@author: danielsalmond
"""
import seaborn as sns; sns.set(style="ticks", color_codes=True)
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import StandardScaler 
from sklearn.neural_network import MLPClassifier 
from sklearn import linear_model

trainFile = "A5_train.csv"
testFile = "A5_test.csv"

train_data = pd.read_csv(trainFile, converters={'Sex':lambda s: ['male','female'].index(s)}).fillna({"Age":-1})
test_data = pd.read_csv(testFile, converters={'Sex':lambda s: ['male','female'].index(s)}).fillna({"Age":-1})


#################################################################################################################
#                                               SURVIVED PREDICTION
#################################################################################################################

features = ["Sex", "Pclass", "Fare"]

Y_survived = train_data["Survived"]
X_survived = train_data[features]

################################################# Decision Tree Algorithm #######################################

decisionTree = DecisionTreeClassifier(min_samples_split=20, random_state=99)
decisionTree.fit(X_survived, Y_survived)

testFeatures = test_data[features]
predictions = decisionTree.predict(testFeatures)

test_data["SDTPredictions"] = decisionTree.predict(testFeatures)

#print(test_data[["Survived", "DTPredictions","Name", "Sex", "Pclass"]])

predicted = test_data.loc[test_data["SDTPredictions"] == test_data["Survived"]]
#print(predicted)


################################################# Neural Network Algorithm ###################################

scaler = StandardScaler()  
scaler.fit(train_data[["Sex","Pclass","Fare"]])

X = scaler.transform(train_data[["Sex","Pclass","Fare"]])
Y = scaler.transform(train_data[["Sex","Pclass","Fare"]])

neuralNet = MLPClassifier(hidden_layer_sizes=(10, 20, 15), max_iter=1000)
neuralNet.fit(X_survived, Y_survived)

testFeatures2 = test_data[features]
predictions2 = neuralNet.predict(testFeatures2)


test_data["SNNPredictions"] = neuralNet.predict(testFeatures2)

#print(test_data[["Survived", "NNPredictions","Name", "Sex", "Pclass"]])

predicted2 = test_data.loc[test_data["SNNPredictions"] == test_data["Survived"]]
#print(predicted2)

################################################# Printed Results ##############################################

print("\nSurvived prediction:")
print("Decision trees:", len(predicted.index), "/", len(test_data.index), sep="")
print("Neural networks:", len(predicted2.index), "/", len(test_data.index), sep="")


#################################################################################################################
#                                                 FARE PREDICTION
#################################################################################################################

#Variables
fareFeatures = ["Pclass", "Sex", "Parch"]

Y_fare = train_data["Fare"].astype(int)
X_fare = train_data[fareFeatures]

Y_test = test_data["Fare"]

################################################# Linear Regression Algorithm ###################################

lm = linear_model.LinearRegression()
model = lm.fit(X_fare, Y_fare)

#LRTestFeatures = test_data[features]
fareTestFeatures = test_data[fareFeatures]
predictions4 = lm.predict(fareTestFeatures)

preds = list(predictions4)

y_test_list = list(Y_test)
#print(y_test_list)

score = lm.score(X_fare,Y_fare)
score = score*100
score = score.round(0)

#the coefficients for the predictors
coefficients = lm.coef_

#the intercept of the model:
intercept = lm.intercept_

#print("Linear regression: ", score, "/", len(test_data.index), sep="")

################################################# Decision Tree Algorithm #######################################

fareDecisionTree = DecisionTreeClassifier(min_samples_split=20, random_state=20)
fareDecisionTree.fit(X_fare, Y_fare)

test_data["FDTPredictions"] = fareDecisionTree.predict(test_data[fareFeatures])
#print(test_data[['Fare', 'FDTPredictions']])
DTTestValue = test_data.loc[np.abs(test_data["FDTPredictions"] - test_data["Fare"].astype(int)) <= 5]
#print(test_data[['Fare', 'FDTPredictions']].astype(int))

################################################# Neural Network Algorithm #####################################

scaler = StandardScaler()  
scaler.fit(X_fare)

X = scaler.transform(train_data[fareFeatures])
Y = scaler.transform(test_data[fareFeatures])

neuralNet = MLPClassifier(hidden_layer_sizes=(20, 20, 20), max_iter=1000)
neuralNet.fit(X, Y_fare)

predictions2 = neuralNet.predict(Y)
test_data["FNNPredictions"] = predictions2

#print(test_data[["Survived", "NNPredictions","Name", "Sex", "Pclass"]])
#predicted2 = test_data.loc[test_data["SNNPredictions"] == test_data["Fare"]]
#print(predicted2)

NNTestValue = test_data.loc[np.abs(test_data["FNNPredictions"] - test_data["Fare"].astype(int)) <= 5]
h = test_data[['Fare', 'FNNPredictions']].astype(int)
#print(h)


################################################# Printed Results ###############################################

print("\nFare prediction:")
print("Linear regression: ", score, "/", len(test_data.index), sep="")
print("Decision trees: ", len(DTTestValue), "/", len(test_data.index), sep="")
print("Neural networks: ", len(NNTestValue.index), "/", len(test_data.index), sep="")
