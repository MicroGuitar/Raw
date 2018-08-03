import cv2
import numpy as np

#read img
raw8 =np.fromfile('2.RAW',np.uint8)
raw8 = raw8.reshape(960,-1)
print raw8
with open('1.RAW', 'rb') as binfile:
  bytestring = list(bytearray(binfile.read()))

a = []

for i in range(0, len(bytestring), 3):
  px_bytes = bytestring[i:i+3]
  p0 = ((px_bytes[0] << 4) | (px_bytes[1] & 0x0F) ) << 4
  p1 = ((px_bytes[2] << 4) | (px_bytes[1] >> 4 & 0x0F) ) << 4
  a.append(p0)
  a.append(p1)

raw12 = np.array(a)
raw12 = raw12.reshape(960,-1)
print raw12
#get mask
#Gauss Blur
GaussianBlur_8 = cv2.GaussianBlur(raw8,(5,5),0)
#Threshold
a,Binary_f = cv2.threshold(GaussianBlur_8,63,255,cv2.THRESH_BINARY)#foreground
a,Binary_b = cv2.threshold(GaussianBlur_8,63,255,cv2.THRESH_BINARY_INV)#background
#create mask
mask_f = cv2.inRange(Binary_f,0,63) #F
mask_b = cv2.inRange(Binary_b,0,63) #B
#get foreground
#8bit normalize
dst_8 = cv2.bitwise_and(raw8,raw8,mask = mask_f)
dst_8test = dst_8.copy()
i = 0
j = 0
while(i < 960):
    while(j < 1280):
        if dst_8test[i,j] == 0:
            dst_8test[i,j] = 10
        j = j + 1
    j = 0    
    i = i + 1
dst8_final = cv2.normalize(dst_8test,None,0,255,cv2.NORM_MINMAX,cv2.CV_8UC1)

#12bit normalize
dst_12 = cv2.bitwise_and(raw12,raw12,mask = mask_f)
dst_12test = dst_12.copy()
i = 0
j = 0
while(i < 960):
    while(j < 1280):
        if dst_12test[i,j] == 0:
            dst_12test[i,j] = 5000
        j = j + 1
    j = 0    
    i = i + 1
dst12_final = cv2.normalize(dst_12test,None,0,65535,cv2.NORM_MINMAX,cv2.CV_16UC1)

print "dst_8 max = ",dst_8.max()
print "dst_12 max = ",dst_12.max()
cv2.imshow('raw8',raw8)
cv2.imshow('raw12',raw12)
cv2.imshow('dst_8',dst_8)
cv2.imshow('dst_12',dst_12)
cv2.imshow('dst8_final',dst8_final)
cv2.imshow('dst12_final',dst12_final)

while(1):
    k = cv2.waitKey(1)&0xFF
    if k == 27 :
        break
cv2.destroyAllWindows()

