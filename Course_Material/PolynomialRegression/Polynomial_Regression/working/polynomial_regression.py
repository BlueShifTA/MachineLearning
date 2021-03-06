#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:,1:2].values
y = dataset.iloc[:,2].values

"""
# Splitting the dataset into the Training set and Test set 
from sklearn.cross_validation import train_test_split 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
"""
"""
# Feature Scaling
from sklearn.preprocessing import StandardScaler

sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test  = sc_X.transform(X_test)
"""

# Fitting Linear Regression 
from sklearn.linear_model import LinearRegression
linrec = LinearRegression()
linrec.fit(X,y)

# Fitting Polynomial Regression
from sklearn.preprocessing import PolynomialFeatures 
poly_reg = PolynomialFeatures(degree = 15)
X_poly = poly_reg.fit_transform(X)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly,y)

# Visualization Linear
plt.scatter(X,y, color = 'red')
plt.plot(X,linrec.predict(X), color = 'blue')

# Visualization Polynomial
plt.scatter(X,y, color = 'red')
plt.plot(X, lin_reg_2.predict(poly_reg.fit_transform(X)), color = 'blue')

# predicting
lin_reg.predict(6.5)