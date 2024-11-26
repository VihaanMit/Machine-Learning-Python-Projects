# -*- coding: utf-8 -*-
"""EDA.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ZN8SGWGicciNFalnE16JcvlKedXMZ7a3
"""

"""
@author Vihaan Mittal

Reference to names of columns (From Kaggle):
"": This is usually the index column, which is often left empty or used to indicate the row number.
crim: Per capita crime rate by town.
zn: Proportion of residential land zoned for lots over 25,000 sq. ft.
indus: Proportion of non-retail business acres per town.
chas: Charles River dummy variable (1 if tract bounds river; 0 otherwise).
nox: Nitric oxides concentration (parts per 10 million).
rm: Average number of rooms per dwelling.
age: Proportion of owner-occupied units built prior to 1940.
dis: Weighted distances to five Boston employment centers.
rad: Index of accessibility to radial highways.
tax: Full-value property tax rate per $10,000.
ptratio: Pupil-teacher ratio by town.
black: 1000(Bk - 0.63)^2 where Bk is the proportion of Black residents by town.
lstat: Percentage of lower status of the population.
medv: Median value of owner-occupied homes in $1000s (this is the target variable).
"""
import pandas as pd
from pandas import set_option
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import Normalizer
from numpy import set_printoptions
import seaborn as sns
from pandas.plotting import scatter_matrix

#Loading Data
data1=pd.read_csv('boston.csv')

#Removing irrelevant 0th index column (Just labels rows by number)
column_names=["","crim","zn","indus","chas","nox","rm","age","dis","rad","tax","ptratio","black","lstat","medv"]
standard_names=column_names[1:14]
data2=data1.drop(data1.columns[0],axis=1)
#Separating data into 'X' and 'Y' or input and output
X = data2.drop(data2.columns[13], axis = 1) # has all other variables
Y = data2.drop(data2.columns[0:13], axis = 1) # only has median house value
print(X)
print(Y)

#Creating a dataframe with all data from csv
df1=pd.DataFrame(data2,columns=standard_names)
print(df1)
df1.hist()
plt.show()

#Gathering descriptive statistics of data
description = df1.describe()
print(description)

#Normalize each column of 'X'
scaler = Normalizer().fit(X)
Normalizeddf1=scaler.transform(X)
df2=pd.DataFrame(Normalizeddf1,columns=standard_names) #Normalized dataframe
print(df2)

#Gathering descriptive stats for normalized data
description = df2.describe()
print(description)

#Look at distribution for each column
set_option('display.width', 100)
df2.hist()
plt.show()

#Standardize each column of data and creating new dataframe out of that
scaler2=StandardScaler().fit(X)
rescaleddata2 = scaler2.transform(X)
df3=pd.DataFrame(rescaleddata2,columns=standard_names) #Standardized dataframe
print(df3)

#Gathering descriptive stats for standardized data
description = df3.describe()
print(description)
df3.hist()
plt.show()

#Creating heatmap
plt.figure()
corMat = df1.corr(method='pearson')
sns.heatmap(corMat, square=True)
plt.title("Correlation Heatmap")
plt.show()

#Creating scatterplot matrix
plt.figure()
scatter_matrix(X)
plt.show()

#Studying scatterplots with line of best fit, specifically in relation to median house val
for i in standard_names:
  sns.regplot(x=i,y='medv',data=data2)
  plt.grid(True)
  plt.show()
  #Printing correlation coefficient along with plots in relation to median house value
  print(data2[i].corr(data2['medv']))