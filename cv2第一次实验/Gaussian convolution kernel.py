import numpy as np
import matplotlib.pyplot as plt
import math

def gaussiankernel(size):
    sigma=0.5
    gaussiankernel=np.zeros((size,size),np.float32)
    for i in range (size):
        for j in range (size):
            norm=math.pow(i-1,2)+pow(j-1,2)
            gaussiankernel[i,j]=math.exp(-norm/(2*math.pow(sigma,2)))
    sum=np.sum(gaussiankernel)
    kernel=gaussiankernel/sum
    return kernel

plt.imshow(gaussiankernel(5),cmap='CMRmap')
plt.show()