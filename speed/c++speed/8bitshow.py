import numpy as np
import cv2

def Read_Raw8(path):

    imgData = np.fromfile(path,np.uint8)

    #imgData = imgData.reshape(960,-1)
    # imgData.tofile('raw8.raw')
    return imgData


img = Read_Raw8("new.RAW")
print img.shape
# cv2.imshow('1',img)
# cv2.waitKey()
# cv2.destroyAllWindows()
