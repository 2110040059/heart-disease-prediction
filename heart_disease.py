# -*- coding: utf-8 -*-
"""Heart disease

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1d11id36kvo0TvLvmVJhm_OBu1I8Tsr4L

# **HEART DISEASE PREDICTION**- TASK 1
"""

import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import warnings
warnings.filterwarnings('ignore')

heart_data = pd.read_csv('heart.csv')
heart_data

heart_data.shape #Printing the shape of dataset

heart_data.info()

heart_data.isnull().sum()

heart_data.describe()

heart_data['target'].value_counts()

x = heart_data.drop(columns = 'target' , axis=1)
y = heart_data['target']

print(x)

print(y)

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.75,stratify=y, random_state =2)

print(x_train)

print(x_test)

print(x_test.shape)

model = LogisticRegression()

model.fit(x_train, y_train)

heart_data['target'].value_counts()

X = heart_data.drop(columns = 'target', axis = 1)
X.head()

Y = heart_data['target']
Y.head()

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.15, stratify = Y, random_state = 3 )

print(X.shape, X_train.shape, X_test.shape)

model = LogisticRegression()

model.fit(X_train.values, Y_train)

X_train_prediction = model.predict(X_train.values)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)

print("The accuracy of training data : ", training_data_accuracy)

import matplotlib.pyplot as plt
plt.figure(figsize=(4,4))
plt.scatter(Y_train, X_train_prediction , color = 'red')
plt.title(" Heart Disease Prediction model fitting ")
plt.show()

X_test_prediction = model.predict(X_test.values)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)

print("The accuracy of test data : ", test_data_accuracy)

# input feature values
input_data = (42,1,0,136,315,0,1,125,1,1.8,1,0,1)

# change the input data into numpy array

input_data_as_numpy_array = np.array(input_data)

# reshape the array to predict data for only one instance

reshaped_array = input_data_as_numpy_array.reshape(1,-1)

# predicting the result and printing it

prediction = model.predict(reshaped_array)

print(prediction)

if(prediction[0] == 1):
    print("Patient has a healthy heart 💛")

else:
    print("Patient has an unhealthy heart 💔")