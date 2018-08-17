import numpy as np
import cv2
import time

def Read_Raw12(path):
    with open(path, 'rb') as binfile:
        bytestring = list(bytearray(binfile.read()))

    a = []
    for i in range(0, len(bytestring), 3):
        px_bytes = bytestring[i:i + 3]
        p0 = ((px_bytes[0] << 4) | (px_bytes[1] & 0x0F)) << 4
        p1 = ((px_bytes[2] << 4) | (px_bytes[1] >> 4 & 0x0F)) << 4
        a.append(p0)
        a.append(p1)

    img = np.array(a)

    imgData12 = img.reshape(-1, 1280)
    i = 0
    print bytestring[1]
    print "******************"
    for i in range (0,10):
        #print bytestring[i]
        print imgData12[0][i]
    print imgData12    
    return imgData12  

img = Read_Raw12('./1.RAW') 

#print img
cv2.imshow('raw12',img)
cv2.waitKey()
cv2.destroyAllWindows() 

