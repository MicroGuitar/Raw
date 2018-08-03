import numpy as np
import cv2

def nothing(x):
    pass

#read image
img_raw8 = np.fromfile('test.RAW' ,dtype = np.uint8 )
img_raw8 = img_raw8.reshape(960,1280,1)
#read image
img_png = cv2.imread('test.BMP',0)

# blur & GaussianBlur
Gaussianblur = cv2.GaussianBlur(img_raw8,(5,5),0)
# blur = cv2.blur(img_raw8,(7,7))
Gaussianblur_png = cv2.GaussianBlur(img_png,(5,5),0)
# blur_png = cv2.blur(img_png,(7,7))

#create window & trackbar
cv2.namedWindow('bmp_canny')
cv2.namedWindow('raw_canny') 

cv2.createTrackbar('PNG-Low Threshold','bmp_canny',10,255,nothing)
cv2.createTrackbar('PNG-High Threshold','bmp_canny',30,255,nothing)

cv2.createTrackbar('RAW-Low Threshold','raw_canny',10,255,nothing)
cv2.createTrackbar('RAW-High Threshold','raw_canny',30,255,nothing)

#process
while(1):
    Low_png = cv2.getTrackbarPos('PNG-Low Threshold','bmp_canny')
    High_png = cv2.getTrackbarPos('PNG-High Threshold','bmp_canny')
    Low_raw = cv2.getTrackbarPos('RAW-Low Threshold','raw_canny')
    High_raw = cv2.getTrackbarPos('RAW-High Threshold','raw_canny')    

    Canny_png = cv2.Canny(Gaussianblur_png,Low_png,High_png)
    Canny = cv2.Canny(Gaussianblur,Low_raw,High_raw)

    cv2.imshow('bmp_canny',Canny_png)
    cv2.imshow('raw_canny',Canny)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    else :continue



# cv2.imshow('img_raw8',img_raw8)
# cv2.imshow('img_png',img_png)

cv2.destroyAllWindows() 