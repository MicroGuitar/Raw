from bitstring import BitArray as Bit
import numpy as np
import cv2
import matplotlib.pyplot as plt

with open('1.RAW', 'rb') as binfile:
  bytestring = list(bytearray(binfile.read()))

a = []

for i in range(0, len(bytestring), 3):
  px_bytes = bytestring[i:i+3]
  p0 = ((px_bytes[0] << 4) | (px_bytes[1] & 0x0F) ) << 4
  p1 = ((px_bytes[2] << 4) | (px_bytes[1] >> 4 & 0x0F) ) << 4
  a.append(p0)
  a.append(p1)

img = np.array(a)
imgData = img.reshape(960,-1)
print bin(imgData[55,55])
#print (imgData[58,58]/256.0)
#imgData[0,0] = 4095
#imgData = cv2.normalize(imgData, None, 0,65535, cv2.NORM_MINMAX, cv2.CV_16UC1).astype('uint16')
#print imgData[50,50]
# imgData_t = (imgData/4096.0)*65536
# print type(imgData_t[0,0])
# imgData_t = imgData_t.astype(np.uint16)
# print type(imgData_t[0,0])
# print imgData_t
# print imgData_t[0,0]

# with open('2.RAW', 'rb') as binfile:
#   bytestring1 = list(bytearray(binfile.read()))

# a1 = []

# for i in range(0, len(bytestring1), 3):
#   px_bytes1 = bytestring1[i:i+3]
#   p01 = (px_bytes1[0] << 4) | (px_bytes1[1] & 0x0F)
#   p11 = (px_bytes1[2] << 4) | (px_bytes1[1] >> 4 & 0x0F)
#   a1.append(p01)
#   a1.append(p11)

# img1 = np.array(a1)

# imgData1 = img1.reshape(960,-1,1)

# imgData1 = cv2.normalize(imgData1, None, 0,65536, cv2.NORM_MINMAX, cv2.CV_16UC1).astype('uint16')

##################################
raw8 = np.fromfile('2.RAW',np.uint8)

raw8 = raw8.reshape(960,-1)
print bin(raw8[55,55])
cv2.imshow('raw8',raw8)



cv2.imshow('raw12',imgData)
#cv2.imshow('img1',imgData1)
cv2.waitKey()
cv2.destroyAllWindows() 
# plt.figure()
# plt.subplot(1,3,1)
# plt.imshow(imgData,cmap='Greys_r')
# plt.subplot(1,3,2)
# plt.imshow(imgData1,cmap='Greys_r')
# plt.subplot(1,3,3)
# plt.imshow(BGR,cmap='Greys_r')
# plt.show()
