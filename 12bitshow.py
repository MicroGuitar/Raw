from bitstring import BitArray as Bit
import numpy as np
import cv2

with open('12bitraw.RAW', 'rb') as binfile:
  bytestring = list(bytearray(binfile.read()))

a = []

e1 = cv2.getTickCount()
for i in range(0, len(bytestring), 3):
  px_bytes = bytestring[i:i+3]
  p0 = (px_bytes[0] << 4) | (px_bytes[1] & 0x0F)
  p1 = (px_bytes[2] << 4) | (px_bytes[1] >> 4 & 0x0F)
  a.append(p0)
  a.append(p1)

e2 = cv2.getTickCount()
t = (e2 - e1)/cv2.getTickFrequency()
print t

img = np.array(a)

print img.size

imgData = img.reshape(960,-1,1)

imgData = cv2.normalize(imgData, None, 0,65536, cv2.NORM_MINMAX, cv2.CV_16UC1).astype('uint16')

cv2.imshow('img',imgData)
cv2.waitKey()
cv2.destroyAllWindows() 
