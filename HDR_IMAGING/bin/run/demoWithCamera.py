#!/usr/bin/python2.7
# -*- coding:utf-8 -*-
__author__ = 'gimbu'
__data__ = '30/03/17'

# import sys
# sys.path.append('../')
from MVCamLib.MVCam_py import MVCam
import cv2
import numpy as np
import time
import matplotlib.pyplot as plt
from aux_lib import FileInterfaceTool as fit
from HDR import HDR as ht
# import cProfile
# import re

if __name__ == '__main__':
    MVCam1 = MVCam()
    if not MVCam1.EnumerateDevice():
        print 'Cannot find any cameras!'
        exit(-1)
    resolution = (480, 480)
    cam_list = MVCam1.Getname()
    cam_list = cam_list.split(',')
    print '-------------------------------------------------'
    print 'There are all cameras we Found!'
    object = enumerate(cam_list)
    for i, name in object:
        print "%d " % i + name
    print 'Please input 0~%d to open camera:' % (len(cam_list)-1),
    cam_name = cam_list[0]
    hCam = MVCam1.Init(cam_name)
    print 'hCam', hCam
    MVCam1.SetAeState(hCam, False)
    print 'SetAnalogGain', MVCam1.SetAnalogGain(hCam, 100)
    print 'SetImageResolution', MVCam1.SetImageResolution(hCam, resolution[0], resolution[1])
    print 'SetTriggerMode', MVCam1.SetTriggerMode(hCam, 1)
    print 'CameraSetTriggerCount', MVCam1.SetTriggerCount(hCam, 1)
    print 'Play', MVCam1.Play(hCam)
    #---------------necessary--------------------
    while True:
        img = MVCam1.getImage(hCam, 1000)
        if img is None:
            break
    #---------------necessary--------------------

    path = "./configure/"
    filename = "hdr_configure.yaml"
    arg_list = fit.loadYaml(path + filename)
    img_output_path = arg_list["OutputPath"]

    cali_gamma = arg_list["cali_gamma"]
    LDR_SIZE = arg_list["LDR_SIZE"]
    merge_gamma = arg_list["merge_gamma"]
    contrast = arg_list["contrast"]
    saturation = arg_list["saturation"]
    sigma_space = arg_list["sigma_space"]
    sigma_color = arg_list["sigma_color"]

    wcon = arg_list["wcon"]
    wsat = arg_list["wsat"]
    wexp = arg_list["wexp"]

    index = 0
    FirstFlag = True
    hdr_merge = ht.HdrMerge(
                       merge_gamma, contrast, saturation, sigma_space, sigma_color)
    hdr_fusion = ht.HdrFusion(wcon, wsat, wexp)
    Group_count = 0
    while True:
        exposure_time = [5000, 51000, 100000]
        times = [0.005, 0.051, 0.100]
        images = []
        key = None
        stack_img = None
        for et in exposure_time:
            print "setting exposure_time: %s" % et
            MVCam1.SetExposureTime(hCam, et)
            print "SoftTrigger", MVCam1.SoftTrigger(hCam)
            img0 = MVCam1.getImage(hCam, 1000)
            img0 = cv2.cvtColor(img0, cv2.COLOR_BGR2GRAY)
            img0 = cv2.cvtColor(img0, cv2.COLOR_GRAY2BGR)
            # img0 = cv2.imread("saved_img/gray_img"+str(et)+".png")
            images.append(img0)
        stack_img = np.hstack((images[0], images[1]))
        stack_img = np.hstack((stack_img, images[2]))
        cv2.putText(stack_img, "Group Image "+str(Group_count),
                    (150, 400), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 0), 2)
        Group_count += 1
        cv2.imshow(cam_name, stack_img)
        key = chr(cv2.waitKey(1) & 0xff)
        if key in ['q', 'Q']:
            print "destroy all windows", cv2.destroyAllWindows()
            print '\nUnInit', MVCam1.UnInit(hCam)
            break
        if FirstFlag == True:
            hdr_merge.preprocess(cali_gamma, LDR_SIZE, images, times)
            FirstFlag = False
        ldr_img = hdr_merge.process(images, times)
        cv2.imshow("realtime hdrmerge", ldr_img)
        fusion_img = hdr_fusion.process(images)
        cv2.imshow("realtime hdrfusion", fusion_img)
