#Author: Daniel Zuñiga @ Virgilio Barco Library, Bogotá

#Libraries import
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

twitter_data = pd.read_csv('result.csv')

#Correlates all variables of the data frame and shows result
print(twitter_data.corr())

#Allows to see a plot of the correlation of two variables.
    #The X-axis represents # of followers.
    #The Y-axis represents # of friends.
plt.scatter(twitter_data.friends, twitter_data.followers)

#Outcome
Y = twitter_data.followers
#Predictor
X = twitter_data.friends
#Constant
X = sm.add_constant(X)

#Gets the linear regression model.
lr_model = sm.OLS(Y, X).fit()

#Print a summary of the model. There we'll find the constant and the coeficient
#   of the linear regression equation: likeCount = coeff * viewCount + const
print(lr_model.summary())

#Generates 100 values between the minimun and maximun of viewCount values.
X_prime = np.linspace(X.friends.min(), X.friends.max(), 100)
X_prime = sm.add_constant(X_prime)
#For each generated point predicts the likeCount.
y_hat = lr_model.predict(X_prime)

#Plots the real data and a line showing the linear model
plt.scatter(X.friends, Y)
plt.xlabel("# of friends")
plt.ylabel("# of followers")
plt.plot(X_prime[:,1], y_hat)
