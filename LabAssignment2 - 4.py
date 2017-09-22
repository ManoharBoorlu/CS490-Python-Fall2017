import numpy as np                             #importing numpy library as np

d = np.random.random(15)                       # creating a random vector of size 15
d[d.argmax()] = 100                            # changing the maximum value of vector to 100
print("The random vector with size 15 and maximum value as 100 is \n", d)