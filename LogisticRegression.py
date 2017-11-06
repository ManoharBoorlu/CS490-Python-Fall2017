import tensorflow as t
import numpy as n
from sklearn import datasets
import matplotlib.pyplot as p       #Importing the all required libraries and modules

d = datasets.load_diabetes()        #Loading the Diabetes Dataset

diab_x = d.data[:32, 2]             #Considering first 32 elements and 2nd row for X
diab_x = n.asarray(diab_x)          #Converting normal list to a numpy array
diab_y = d.target[:32]              #Considering first 32 elements and target for Y
diab_y = n.asarray(diab_y)          #Converting normal list to a numpy array

diab_data = n.column_stack((diab_x, diab_y))    #Merging X and Y to single numpy array
cnt = len(diab_y)                                  #Finding out length of Y

X = t.placeholder(t.float32, name='X')          #Creating placeholder for X Tensor
Y = t.placeholder(t.float32, name='Y')          #Creating placeholder for X Tensor

w = t.Variable(0.0, name='weight')              #Creating variable for Weights
b = t.Variable(0.0, name='bias')                #Creating variable for Bias


Y_pred = t.nn.softmax(t.multiply(w, X) + b)     #Implementing Logistic Regression using softmax function

loss = t.square(Y - Y_pred, name='loss')        #Implementing the loss

optim = t.train.GradientDescentOptimizer(learning_rate=0.00001).minimize(loss)  #Implementing the optimization factor, Gradient Descent

with t.Session() as s:          #Session Initialization
    s.run(t.global_variables_initializer()) #Initialize w and b
    #wr = t.summary.FileWriter(s.graph)

    for i in range(50):             #Loop to for training 50 epochs
        tot_loss = 0                #Initializing total loss to 0
        for x, y in diab_data:      #Training Loop
            _, L = s.run([optim, loss], feed_dict={X: x, Y: y})
            tot_loss += L
        print('Epoch {0}:{1}'.format(i, tot_loss/cnt))
    #wr.close()

    w,b = s.run([w,b])              #Running the Session