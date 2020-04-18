import  numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
'''
计算绘制一幅彩色图像的红色通道的颜色直方图
'''
img = cv.imread("new.jpg")
img_red = cv.cvtColor(img,cv.COLOR_BGR2RGB)
'''
分离出红色通道
'''
redI = np.zeros_like(img)
redI[:,:,2] = img[:,:,2]

cv.imshow('IMG',redI)
cv.waitKey(0)

red_levels=np.arange(0,256,1)#表示以0为起点,256为终点,步长为一
N_x=np.zeros_like(red_levels,dtype=np.float)#生成与给定数组相同类型和形状的零数组

for(i,level) in enumerate(red_levels):
    N_x[i] = np.sum(img==level)#np.sum返回了等于level的img
plt.plot(red_levels,N_x)
plt.xlabel('bins==256 red levels step length=1')
plt.ylabel('Counted pixel numbers in each level')
plt.title('Grau Hidtogram')
plt.show()