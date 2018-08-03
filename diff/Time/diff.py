import cv2
import numpy as np

imgraw = np.fromfile('sharp60.RAW',np.uint8)

imgraw = imgraw.reshape(960,-1)

imgraw1 = np.fromfile('sharp30.RAW',np.uint8)

imgraw1 = imgraw1.reshape(960,-1)
diff = imgraw1 - imgraw
print diff
cv2.imshow('diff',diff)
cv2.imshow('diff1',imgraw)
cv2.imshow('diff2',imgraw1)
cv2.waitKey()
cv2.destroyAllWindows()

# imgbmp = cv2.imread('test.BMP',0)

# diff = imgraw - imgbmp
# print diff.sum()

# cv2.imshow('diff',diff)
# cv2.imshow('raw',imgraw)
# cv2.imshow('bmp',imgbmp)
# cv2.waitKey()
# cv2.destroyAllWindows()