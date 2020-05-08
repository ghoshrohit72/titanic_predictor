# -*- coding: utf-8 -*-
"""Feature Engineering.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rbjFoA6ahfJG2Fx5gjqPZNoamsGGb2L3
"""

import pandas as pd
import sklearn.model_selection 
from sklearn.model_selection import train_test_split
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv('train.csv')

def get_title(name):
  if '.' in name:
    return name.split(',')[1].split('.')[0].strip()
  else:
      return ('Unknown')

#Normalize titles into different categories
def replace_titles(x):
  title = x['Title']
  if title in ['Capt', 'Col','Major']:
    return 'Officer'
  elif title in ['Don', 'Dona','the Countess','Lady','Master','Jonkheer','Sir']:
    return 'Royalty'
  elif title == 'Mme':
    return 'Mrs'
  elif title in ['Mlle','Ms']:
    return 'Miss'
  else :
    return title


df['Title']= df['Name'].map(lambda x : get_title(x))
df['Title'] =df.apply(replace_titles,axis=1)

df['Age'].fillna(df['Age'].median(), inplace = True)
df['Fare'].fillna(df['Fare'].median(),inplace =True)
df['Embarked'].fillna('S', inplace=True)
df.drop('Cabin', axis=1,inplace=True)
df.drop('Ticket', axis=1, inplace= True)
df.drop('Name', axis=1, inplace=True)
df.Sex.replace(('male', 'female'), (0,1),inplace=True)
df.Embarked.replace(('S','C','Q'), (0,1,2), inplace= True)
df.Title.replace(('Mr', 'Mrs','Miss','Master','Dr','Rev','Officer','Royalty'),(0,1,2,3,4,5,6,7), inplace=True)

x= df.drop(['Survived', 'PassengerId'], axis=1)
y= df['Survived']
x_train, x_val, y_train, y_val=train_test_split(x, y, test_size= 0.1)  #putting 10 % of my data in my validation train

randomforest = RandomForestClassifier()
randomforest.fit(x_train, y_train)  #training the model with 10 % of the data in the above step
pickle.dump(randomforest, open('titanic_model.sav', 'wb'))   #saving the model we have created wb = wide binary



prediction_model(1,1,28,1,1,19,0,1)
