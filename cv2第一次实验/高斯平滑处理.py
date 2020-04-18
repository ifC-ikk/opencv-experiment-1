from scipy import misc
from scipy import ndimage as im
import cv2 as cv
'''
高斯平滑处理
'''
img = cv.imread("new.jpg")
Img1=im.gaussian_filter(img,sigma=10)
Img2=im.gaussian_filter(img,sigma=-18,order=0,output=None,mode='reflect',cval=0.0,truncate=4.0)
'''
imput=img 代表输入数组 sigma高斯核的标准差 order顺序0,1,2,3代表第一二三四个高斯分子的导数
output输出数组可选  mode为模式有reflect  constant mirror等 cval标量可选 truncate截断浮动的标准差,默认值是4
'''
cv.imshow('Img',Img2)
cv.waitKey(0)
cv.imshow('img',Img1)
cv.waitKey(0)



