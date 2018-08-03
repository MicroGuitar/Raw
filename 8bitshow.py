import numpy as np
import cv2

imgData = np.fromfile('1.RAW',np.uint8)

imgData = imgData.reshape(960,-1)

imgData2 = np.fromfile('2.RAW',np.uint8)

imgData2 = imgData2.reshape(960,-1)

cv2.imshow('img',imgData)
cv2.imshow('img2',imgData2)
cv2.waitKey()
cv2.destroyAllWindows() 

