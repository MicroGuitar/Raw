import numpy as np
import cv2

def nothing(x):
    pass

#read png image
img_png = cv2.imread('8bitpng.png')

#read raw8 image
img_raw8 = np.fromfile('8bitraw.RAW' ,dtype = np.uint8 )
img_raw8 = img_raw8.reshape(960,1280,1)

#read raw12 image
with open('12bitraw.RAW', 'rb') as binfile:
  bytestring = list(bytearray(binfile.read()))

a = []

for i in range(0, len(bytestring), 3):
    px_bytes = bytestring[i:i+3]
    p0 = (px_bytes[0] << 4) | (px_bytes[1] & 0x0F)
    p1 = (px_bytes[2] << 4) | (px_bytes[1] >> 4 & 0x0F)
    a.append(p0)
    a.append(p1)

img = np.array(a)

img_raw12 = img.reshape(960,-1,1)

img_raw12 = cv2.normalize(img_raw12, None, 0,65536, cv2.NORM_MINMAX, cv2.CV_16UC1).astype('uint16')


# GaussianBlur
Gaussianblur_raw8 = cv2.GaussianBlur(img_raw8,(5,5),0)
Gaussianblur_png = cv2.GaussianBlur(img_png,(15,15),0)
Gaussianblur_raw12 = cv2.GaussianBlur(img_raw12,(5,5),0)

#create window & trackbar
cv2.namedWindow('png_canny')
cv2.namedWindow('raw8_canny') 
cv2.namedWindow('raw12_canny')
#png
cv2.createTrackbar('PNG-Low Threshold','png_canny',10,255,nothing)
cv2.createTrackbar('PNG-High Threshold','png_canny',16,255,nothing)
#raw8
cv2.createTrackbar('RAW8-Low Threshold','raw8_canny',10,255,nothing)
cv2.createTrackbar('RAW8-High Threshold','raw8_canny',30,255,nothing)
#raw12
cv2.createTrackbar('RAW12-Low Threshold','raw12_canny',10,65536,nothing)
cv2.createTrackbar('RAW12-High Threshold','raw12_canny',100,65536,nothing)

sobelx = cv2.Sobel(img_raw12,cv2.CV_16SC1,1,0)
sobely = cv2.Sobel(img_raw12,cv2.CV_16SC1,0,1)

#process
while(1):
    Low_png = cv2.getTrackbarPos('PNG-Low Threshold','png_canny')
    High_png = cv2.getTrackbarPos('PNG-High Threshold','png_canny')
    Low_raw = cv2.getTrackbarPos('RAW8-Low Threshold','raw8_canny')
    High_raw = cv2.getTrackbarPos('RAW8-High Threshold','raw8_canny')    
    Low_raw12 = cv2.getTrackbarPos('RAW12-Low Threshold','raw12_canny')
    High_raw12 = cv2.getTrackbarPos('RAW12-High Threshold','raw12_canny')

    Canny_png = cv2.Canny(Gaussianblur_png,Low_png,High_png)
    Canny_raw8 = cv2.Canny(Gaussianblur_raw8,Low_raw,High_raw)
    Canny_raw12 = cv2.Canny(sobelx,sobely,Low_raw12,High_raw12)

    cv2.imshow('png_canny',Canny_png)
    cv2.imshow('raw8_canny',Canny_raw8)
    cv2.imshow('raw12_canny',Canny_raw12)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    else :continue

cv2.destroyAllWindows() 