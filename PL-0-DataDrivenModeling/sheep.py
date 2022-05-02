import matplotlib.pyplot as plt
from scipy.stats import *
import numpy as np
from sklearn.linear_model import LinearRegression
import pandas as pd
x = np.array([1814,1824,1834,1844,1854,1864])
y = np.array([125,275,830,1200,1750,1650])
s = linregress(x,y)

#poly3 = np.polyfit(x,y,10)
poly10 = np.polyfit(x,y,4)

#y_pred5 = np.polyval(poly10,x)
y_pred10 = np.polyval(poly10,x)

#plt.plot(x,y_pred,"b-")
plt.plot(x,y_pred10,"y-")
plt.plot(x,y)

#plt.plot([1,2,3,4])
plt.show()
absError = y_pred10 - y

SE = np.square(absError) # squared errors
MSE = np.mean(SE) # mean squared errors
RMSE = np.sqrt(MSE) # Root Mean Squared Error, RMSE
Rsquared = 1.0 - (np.var(absError) / np.var(y))
print('RMSE:', RMSE)
print('R-squared:', Rsquared)
print("valor para 10 anos a mais :" + y_pred10 )
