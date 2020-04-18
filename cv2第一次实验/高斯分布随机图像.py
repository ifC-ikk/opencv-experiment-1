import matplotlib.pyplot as plt
import numpy as np

mean=(0,1)
cov=[[1,0],[0,1]]
x=np.random.multivariate_normal(mean,cov,(50,50),'raise')#x随机数

def gauss1d(x, mean, sigma):
    '''
    1d gaussian with mean and sigma
    :param x:
    :param mean:
    :param sigma:
    :return fx:
    '''
    dist = (x-mean)**2
    stand_dist = dist/(2*sigma**2)
    fx = np.exp(-stand_dist)/(np.sqrt(2*np.pi)*sigma)
    return fx

#x  = np.arange(-10, 10, 0.001)
x1 = np.linspace(-5, 5, 1000)
fx = gauss1d(x1, mean=0, sigma=1)#y随机数

plt.plot(x1, fx)
plt.hist(x[:,:,0],bins=6)
'''
plt.hist(x为数据,bins为条形数,color,density,range,bottom,histtype,align)
'''
plt.show()
