import numpy as np
import cv2
from matplotlib import pyplot as plt

imgL = cv2.imread('1.png',0)
cv2.imshow('imgL', imgL)
imgR = cv2.imread('2.png',0)
cv2.imshow('imgR', imgR)

stereo = cv2.StereoBM_create(numDisparities=16, blockSize=15)
disparity = stereo.compute(imgL,imgR)
plt.imshow(disparity,'gray')
for i in disparity:
	print(i)
plt.show()