import cv2
import numpy as np

imgraw_0 = np.fromfile('0.RAW',np.uint8)

imgraw_0 = imgraw_0.reshape(960,-1)

imgraw_50 = np.fromfile('50.RAW',np.uint8)

imgraw_50 = imgraw_50.reshape(960,-1)

imgraw_90 = np.fromfile('90.RAW',np.uint8)

imgraw_90 = imgraw_90.reshape(960,-1)

diff1 = imgraw_0 - imgraw_50
print diff1.sum()

diff2 = imgraw_0 - imgraw_90
print diff2.sum()

diff3 = imgraw_90 - imgraw_50
print diff3.sum()

cv2.imshow('diff',diff1)
cv2.imshow('diff2',diff2)
cv2.imshow('diff3',diff3)
cv2.waitKey()
cv2.destroyAllWindows()