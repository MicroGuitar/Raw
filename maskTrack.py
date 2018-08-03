import cv2
import numpy as np

def nothing(x):
    pass
# with open('1.RAW', 'rb') as binfile:
#   bytestring = list(bytearray(binfile.read()))

# a = []

# for i in range(0, len(bytestring), 3):
#   px_bytes = bytestring[i:i+3]
#   p0 = ((px_bytes[0] << 4) | (px_bytes[1] & 0x0F) ) << 4
#   p1 = ((px_bytes[2] << 4) | (px_bytes[1] >> 4 & 0x0F) ) << 4
#   a.append(p0)
#   a.append(p1)

# img = np.array(a)
# imgData = img.reshape(960,-1)
#print bin(imgData[55,55])

raw8 = np.fromfile('2.RAW',np.uint8)
raw8 = raw8.reshape(960,-1)
print type(raw8)
Gaussianblur = cv2.GaussianBlur(raw8,(5,5),0)
#Binary = cv2.adaptiveThreshold(raw8,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
qqq,Binary = cv2.threshold(Gaussianblur,45,255,cv2.THRESH_BINARY)
cv2.namedWindow('binary')
cv2.createTrackbar('threshold','binary',45,255,nothing)
while(1):
    threshold = cv2.getTrackbarPos('threshold','binary')
    #print threshold
    qqq,Binary = cv2.threshold(Gaussianblur,threshold,255,cv2.THRESH_BINARY)
    cv2.imshow('binary',Binary)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    else :continue
cv2.imshow('binary',Binary)
cv2.waitKey()
cv2.destroyAllWindows()