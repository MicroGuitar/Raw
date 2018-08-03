import cv2 as cv
 
import numpy as np
 
import matplotlib.pyplot as plt

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
# im_gray = img.reshape(960,-1)

imgData = np.fromfile('2.RAW',np.uint8)
import cv2 as cv
 
import numpy as np
 
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
im_gray = img.reshape(960,-1)

# imgData = np.fromfile('2.RAW',np.uint8)

# im_gray = imgData.reshape(960,-1)


#im_gray = cv.imread('messi.jpg',0)

cv.imshow('im_gray',im_gray)
cv.waitKey()
 
w = im_gray.shape[0]
 
h = im_gray.shape[1]
 
print im_gray
 
p1 = plt.hist(im_gray.reshape(im_gray.size,1),bins = 20)
 
#plt.subplot(121)
 
plt.show()
 
n = np.zeros((65536),dtype = np.float)
 
p = np.zeros((65536),dtype = np.float)
 
c = np.zeros((65536),dtype = np.float)
 
for x in range(0,im_gray.shape[0]):
 
    for y in range(0,im_gray.shape[1]):
 
        n[im_gray[x][y]] += 1
 
print n

for i in range(0,65536):
 
    p[i] = n[i]/float(im_gray.size)
 
c[0] = p[0]
 
for i in range(1,65536):
 
    c[i] = c[i-1]+p[i]
 
print c
 
des = np.zeros((w,h),dtype=np.uint16)
 
for x in range(0,w):
 
    for y in range(0,h):
 
        des[x][y] = 65535*c[im_gray[x][y]]
 
print des
 
cv.imshow('des',des)
cv.waitKey()
cv.destroyAllWindows()
 
p2 = plt.hist(des.reshape(des.size,1),bins = 20)

plt.show()
im_gray = imgData.reshape(960,-1)


#im_gray = cv.imread('messi.jpg',0)

cv.imshow('im_gray',im_gray)
cv.waitKey()
 
w = im_gray.shape[0]
 
h = im_gray.shape[1]
 
print im_gray
 
p1 = plt.hist(im_gray.reshape(im_gray.size,1),bins = 20)
 
#plt.subplot(121)
 
plt.show()
 
n = np.zeros((256),dtype = np.float)
 
p = np.zeros((256),dtype = np.float)
 
c = np.zeros((256),dtype = np.float)
 
for x in range(0,im_gray.shape[0]):
 
    for y in range(0,im_gray.shape[1]):
 
        n[im_gray[x][y]] += 1
 
print n

for i in range(0,256):
 
    p[i] = n[i]/float(im_gray.size)
 
c[0] = p[0]
 
for i in range(1,256):
 
    c[i] = c[i-1]+p[i]
 
print c
 
des = np.zeros((w,h),dtype=np.uint8)
 
for x in range(0,w):
 
    for y in range(0,h):
 
        des[x][y] = 255*c[im_gray[x][y]]
 
print des
 
cv.imshow('des',des)
cv.waitKey()
cv.destroyAllWindows()
 
p2 = plt.hist(des.reshape(des.size,1),bins = 20)

plt.show()