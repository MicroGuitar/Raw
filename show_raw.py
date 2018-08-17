import numpy as np
import cv2
import time

def Read_Raw8(path):
    imgData = np.fromfile(path,np.uint8)

    imgData = imgData.reshape(960,-1)
    # imgData.tofile('raw8.raw')
    return imgData

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

    imgData12 = img.reshape(960, -1)

    return imgData12

a = time.time()
Read_Raw12('./1.RAW')
b = time.time()
print b - a 