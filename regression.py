# -*- coding: utf-8 -*-
"""Regression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HCvJk-ZxnrDMKW7JBu1pjhSAMztmIvfJ
"""

import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

#problem data
t=np.array([5,7,12,16,20]).reshape(-1,1) #Feature matrix (independent varaible )
m=np.array([40,120,180,210,240]) #target vector (dependent varaible)

lr=LinearRegression()#create a linear regression
lr.fit(t,m)# fit the model to the data

#plot the data
plt.scatter(t,m,color='black')
#plot linear regression line
y_pred=lr.predict(t) #t=5,7,12,16,20
print(y_pred)
plt.plot(t,y_pred,color='blue',linewidth=3,marker="H")
plt.xlabel("Time")
plt.ylabel("Mass")
plt.title('Linear Regression')
plt.show()

from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
LR=LinearRegression()
t=[[5],[7],[12],[16],[20]]
m=[40,120,180,210,240]
LR.fit(t,m)
LR.predict([[5.5]])
plt.scatter(t,m,color='black')
y_pred = LR.predict([[5.5]])
print(y_pred)
plt.plot(5.5,y_pred,5.5,color='blue',linewidth=3,marker="H")
plt.xlabel('Time')
plt.ylabel('Mass')
plt.title('LinearRegression')
plt.show()

import numpy as np
from sklearn.linear_model import LogisticRegression
#distance and corresponding probability data
distances=np.array([1,2,5,10,15,20,21,22,23,24,25,26,27,28,29,30,35,40,41,47,50]).reshape(-1,1)
probabilities=np.array([1,1,1,1,1,1,0.9,0.85,0.73,0.67,0.5,0.47,0.39,0.31,0.25,0.15,0,0,0,0,0])
#convert probabilities to binary labels
threshold=0
binary_labels=(probabilities>threshold)
#create and fit logistic regression model
logr=LogisticRegression()
logr.fit(distances,binary_labels)

p=logr.predict([[25]])#distance
print(p)

if p==[True]:
  print("Goal")
else:
  print("No Goal")

#predict 100 distances between 1 and 50
#generate distances for prediction
dist=np.linspace(1,50,100).reshape(-1,1)
print(dist)#distances
#make predictions using the model
prob=logr.predict_proba(dist)#probabilities -predict
print(prob)

#plotting actual data -train
import matplotlib.pyplot as plt
plt.scatter(distances,binary_labels,color='black',label='Data')
#plotting test data with predictions-valid/test
plt.plot(dist,prob,color='blue',label='Logistic Regression')
plt.title('Distance vs Probability of Scoring a Goal')
plt.xlabel('Distance')
plt.ylabel('Probability')
plt.legend()
plt.grid(True)
plt.show()

#plotting actual data -train
import matplotlib.pyplot as plt
plt.scatter(distances,binary_labels,color='black',label='Data')
#plotting test data with predictions-valid/test
plt.plot(dist,prob,color='blue',label='Logistic Regression')
plt.title('Distance vs Probability of Scoring a Goal')
plt.xlabel('Distance')
plt.ylabel('Probability')
plt.legend()
plt.grid(False)
plt.show()

import pandas as pd
df=pd.read_csv("/content/drive/MyDrive/demoDT.csv")
print(df)

import numpy as np
#load varaibles as array!
cr=np.array(df[' Crime_Rate']).reshape(-1,1)
y=np.array(df['Good'])

#create the model
from sklearn.linear_model import LogisticRegression
model=LogisticRegression()

#train the model
model.fit( cr,y)

c=int(input("enter crime rate in your city:"))
pred=model.predict([[c]])#crime rate
if pred ==1:
  print("Good city")
else:
  print("Bad city")