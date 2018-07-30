import numpy as np
import cv2

imgData = np.fromfile('8bitshow.RAW',np.uint8)

print imgData.dtype.name
print imgData

imgData = imgData.reshape(960,-1)

print imgData.shape

cv2.imshow('img',imgData)
cv2.waitKey()
cv2.destroyAllWindows() 

