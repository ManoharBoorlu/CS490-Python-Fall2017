from sklearn import linear_model
from sklearn import datasets
import numpy as np
import matplotlib.pyplot as plt
diab = datasets.load_diabetes()
b=diab.data[:,np.newaxis,2]
xtrain=b[:-25]
xtarget=b[-25:]
ytrain=diab.target[:-25]
ytarget=diab.target[-25:]
model=linear_model.LinearRegression()
model.fit(xtrain,ytrain)
ypred=model.predict(xtarget)
plt.scatter(xtarget,ytarget, color='blue')
plt.plot(xtarget,ypred)
plt.title("Prediction using Linear Regression")
plt.show()