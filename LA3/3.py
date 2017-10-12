from sklearn import datasets,metrics
from sklearn import cross_validation as cv
from sklearn import svm

diab = datasets.load_diabetes()                          # Loading the dataset
model = svm.SVC(kernel='linear')                         # Loading SVM Model
x=diab.data
y=diab.target
x_train,x_test,y_train,y_test=cv.train_test_split(x,y,test_size=0.3)   # Splitting testing data as 30%

model.fit(x_train, y_train)                             # fitting training data into model
y_pred=model.predict(x_test)                            # predicting with the testing data
print("Accuracy :", metrics.accuracy_score(y_test,y_pred))            # printing accuracy score

diab = datasets.load_diabetes()                          # Loading the dataset
model = svm.SVC(kernel='rbf')                         # Loading SVM Model
x=diab.data
y=diab.target
x_train,x_test,y_train,y_test=cv.train_test_split(x,y,test_size=0.3)   # Splitting testing data as 30%
model.fit(x_train, y_train)                             # fitting training data into model
y_pred=model.predict(x_test)                            # predicting with the testing data
print("RBF Accuracy :", metrics.accuracy_score(y_test,y_pred))            # printing accuracy score
