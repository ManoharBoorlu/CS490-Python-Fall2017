import numpy as np
import matplotlib.pyplot as plt

x=np.array([0,1,2,3,4,5,6,7,8,9])
y=np.array([1,3,2,5,7,8,8,9,10,12])

xm=np.mean(x)
ym=np.mean(y)

slope=(sum((x-xm)*(y-ym)))/sum((x-xm)*(x-xm))

intercept=ym-(slope*xm)

plt.scatter(x,y,color='b')
plt.plot(x, x*slope + intercept, 'r')
plt.title(slope)
plt.show()