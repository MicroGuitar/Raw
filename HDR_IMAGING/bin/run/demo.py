#!/usr/bin/python2.7
# -*- coding:utf-8 -*-
__author__ = 'gimbu'
__data__ = '30/03/17'
import os
import sys
import cv2
import numpy as np
import time
import matplotlib.pyplot as plt

_FILE_PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(_FILE_PATH, os.path.pardir, os.path.pardir)))

from toolbox import io
from HDR import HDR
# import cProfile
import re

########################################
def Read_Raw8(path):
    imgData = np.fromfile(path,np.uint8)
    imgData = imgData.reshape(960,-1)
    print imgData.shape
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
##############################################

def normalizeROI(img, roi_xyxy):
    from toolbox import imgproctool as ipt
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, roi_img = ipt.getRoiImg(gray_img, roi_xyxy, ipt.ROI_TYPE_XYXY)
    cv2.imshow("a", roi_img)
    max_val = np.max(roi_img)
    min_val = np.min(roi_img)
    roi_img = (roi_img - min_val) / (max_val - min_val) * 255
    roi_img = roi_img.astype(np.uint8)
    cv2.imshow("b", roi_img)
    gray_img[roi_xyxy[1]:roi_xyxy[3], roi_xyxy[0]:roi_xyxy[2]] = roi_img
    return gray_img

if __name__ == '__main__':
    os.chdir(_FILE_PATH)

    time_start = time.time()

    # pr = cProfile.Profile()
    # pr.enable()
    yaml_path = os.path.join(_FILE_PATH, "..", "..", "datas", "input", "hdr_configure.yaml")
    arg_list = io.loadYaml(yaml_path)

    img_input_path = arg_list["InputPath"]
    img_output_path = os.path.join(img_input_path, "result")
    if not os.path.exists(img_output_path):
        os.mkdir(img_output_path)
    img_name_list = arg_list["img_names"]
    print img_input_path+img_name_list[1]
    # print arg_list
    # times = arg_list["times"]
    img_list = []
    for i in xrange(len(img_name_list)):
        # img = cv2.imread(img_input_path+img_name_list[i])
        ###########################
        img = Read_Raw8(img_input_path + img_name_list[i])
        # img = Read_Raw12(img_input_path+img_name_list[i])
        ############################
        img_list.append(img)


    # cv2.imshow("src", img_list[2])
    # res = normalizeROI(img_list[2], (360,476, 438, 560))
    # cv2.imshow("res", res)

    # print "--------------------hdr_merge----------------------"
    # cali_gamma = arg_list["cali_gamma"]
    # LDR_SIZE = arg_list["LDR_SIZE"]
    # merge_gamma = arg_list["merge_gamma"]
    # contrast = arg_list["contrast"]
    # saturation = arg_list["saturation"]
    # sigma_space = arg_list["sigma_space"]
    # sigma_color = arg_list["sigma_color"]
    # #----------------offline--------------------not del
    # # clb = HDR.Calibration(cali_gamma, LDR_SIZE)
    # # camera_response_256x1x3 = clb.process(images, times)
    # # clb.showSaveData("hdr_response_gamma10.txt")
    # #----------------offline--------------------not del
    # hdr_merge = HDR.HdrMerge(
    #                merge_gamma, contrast, saturation, sigma_space, sigma_color)
    # hdr_merge.preprocess(cali_gamma, LDR_SIZE, img_list, times)
    # start = time.time()
    # ldr_img = hdr_merge.process(img_list, times)
    # end = time.time()
    # print "hdr merge spend time: \n%f" % (end-start)
    # try:
    #     os.mkdir(img_output_path)
    # except Exception as e:
    #     print e.message
    # cv2.imwrite(os.path.join(img_output_path+"HdrMerge.png"), ldr_img)
    # cv2.namedWindow("HDR MERGE", cv2.WINDOW_NORMAL)
    # cv2.imshow("HDR MERGE", ldr_img)
    # print "------------------------------------------------"

    print "------------------hdrfusion------------------"
    wcon = arg_list["wcon"]
    wsat = arg_list["wsat"]
    wexp = arg_list["wexp"]
    hdr_fusion = HDR.HdrFusion(wcon, wsat, wexp)
    start = time.time()
    fusion_img = hdr_fusion.process(img_list)
    end = time.time()
    print "hdr fusion spend time: \n%f s" % (end-start)
    fusion_img.tofile(os.path.join(img_output_path,"HdrFusion.raw"))
    cv2.imwrite(os.path.join(img_output_path,"HdrFusion.png"), fusion_img)
    cv2.namedWindow("HDR FUSION", cv2.WINDOW_NORMAL)
    #cv2.namedWindow("HDR FUSION")
    time_end = time.time()
    print time_end-time_start
    cv2.imshow("HDR FUSION", fusion_img)
    #print fusion_img
    print "----------------------------------------------"
    # while (1):
    #     k = cv2.waitKey() & 0xFF
    #     if k == 27:
    #         break
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # cProfile.run('re.compile("HdrAlgorithm")', 'stats')
    # pr.disable()
    # pr.print_stats(sort='time')
    pass

