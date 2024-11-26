# -*- coding: utf-8 -*-
"""decision_tree.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1QQBb1DGDpJtRXW-8ORPuHH5ju5W9THAZ
"""

# -*- coding: utf-8 -*-
"""
@author Vihaan
Decision Tree Homework

Column Descriptions from Kaggle:

AtBat: Number of times at bat in 1986.
Hits: Number of hits in 1986.
HmRun: Number of home runs in 1986.
Runs: Number of runs in 1986.
RBI: Number of runs batted in in 1986.
Walks: Number of walks in 1986.
Years: Number of years in the major leagues.
CAtBat: Number of times at bat during career.
CHits: Number of hits during career.
CHmRun: Number of home runs during career.
CRuns: Number of runs during career.
CRBI: Number of runs batted in during career.
CWalks: Number of walks during career.
League: League in 1986 (A for American, N for National).
Division: Division in 1986 (E for East, W for West).
PutOuts: Number of putouts in 1986.
Assists: Number of assists in 1986.
Errors: Number of errors in 1986.
Salary: Salary in 1987 (in thousands of dollars).
NewLeague: League at the beginning of 1987 (A for American, N for National).
"""
#importing necessary libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn import metrics
from six import StringIO
from IPython.display import Image
from sklearn.tree import export_graphviz
import pydotplus
from sklearn import tree
import matplotlib.pyplot as plt
import seaborn as sns
from pandas.plotting import scatter_matrix

#Loading data
column_names=["AtBat","Hits","HmRun","Runs","RBI","Walks","Years","CAtBat","CHits","CHmRun","CRuns","CRBI","CWalks","League","Division","PutOuts","Assists","Errors","Salary","NewLeague","SalaryLog"]
dataset = pd.read_csv('Baseball_salary.csv')

#Removing null rows
sumNullRws = dataset.isnull().sum()
dataset = dataset.dropna()
dataset.isnull().sum()

#Log transformation of Salary
array = np.log(dataset['Salary'].values)

#Adding SalaryLog to Dataframe
dataset.loc[:,'SalaryLog'] = pd.Series(array, index=dataset.index)
dataset = dataset.dropna()

#EDA
#Creating dataframe and mapping Binary values to 0 and 1
df1=pd.DataFrame(dataset,columns=column_names)
df1['NewLeague']=df1['NewLeague'].map({'A':0,'N':1})
df1['League']=df1['League'].map({'A':0,'N':1})
df1['Division']=df1['Division'].map({'W':0,'E':1})

#Printing data
print(df1)
#Printing Histograms
df1.hist()
plt.show()

#Printing Descriptive Statistics
description = df1.describe()
print(description)

#Creating heatmap
plt.figure()
corMat = df1.corr(method='pearson')
sns.heatmap(corMat, square=True)
plt.title("Correlation Heatmap")
plt.show()

#Creating scatterplot matrix
plt.figure()
scatter_matrix(dataset,alpha=0.2,diagonal='hist',figsize=(20,20))
plt.show()

#Based on EDA, choose 6 features and create dataframe out of them
selected_features=['CAtBat','CHits','CHmRun','CRuns','CWalks','CRBI']
selected_features_df=pd.DataFrame(dataset,columns=selected_features)

dataset.describe()
#Splitting selected_features and SalaryLog
X = dataset.loc[:,selected_features]
y = dataset['SalaryLog']
#Test-train splitting
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,random_state=0)

#Creating and fitting tree model
regressor = DecisionTreeRegressor(max_depth=2)
regressor.fit(X_train, y_train)

#Predicting test data
y_pred = regressor.predict(X_test)
prediction_df=pd.DataFrame({'Actual':y_test, 'Predicted':y_pred})

#Seeing Performance Measures
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test,y_pred)))

#Printing Decision Tree
#Has more than ten features when there is no max_depth
dot_data = StringIO()
export_graphviz(regressor, out_file=dot_data,
filled=True, rounded=True,
special_characters=True)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
Image(graph.create_png())