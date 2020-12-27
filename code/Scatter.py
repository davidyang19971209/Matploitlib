import matplotlib.pyplot as plt
import numpy as np

n = 1024
X = np.random.normal(0,1,n)
Y = np.random.normal(0,1,n)
T = np.arctan2(Y,X)

plt.scatter(X,Y,s=75,c=T,alpha=0.5)

plt.xlim((-3,3))
plt.ylim((-3,3))

plt.show()