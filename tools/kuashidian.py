import cv2
import os
import torch
import numpy as np

import math
import matplotlib.pyplot as plt

img_w = 640
img_h = 480


# 绕cx,cy逆时针旋转
def Nrotate(angle, valuex, valuey, pointx, pointy):
    valuex = np.array(valuex)
    valuey = np.array(valuey)
    nRotatex = (valuex - pointx) * math.cos(angle) - (valuey - pointy) * math.sin(angle) + pointx
    nRotatey = (valuex - pointx) * math.sin(angle) + (valuey - pointy) * math.cos(angle) + pointy
    return nRotatex, nRotatey

# 绕cx,cy顺时针旋转
def Srotate(angle, valuex, valuey, pointx, pointy):
    valuex = np.array(valuex)
    valuey = np.array(valuey)
    sRotatex = (valuex - pointx) * math.cos(angle) + (valuey - pointy) * math.sin(angle) + pointx
    sRotatey = (valuey - pointy) * math.cos(angle) - (valuex - pointx) * math.sin(angle) + pointy
    return sRotatex, sRotatey
# 中心点坐标需要修改 ，针对不同的尺寸
def dsd(cx, cy, old_view, new_view, frame):
    if old_view <= new_view:
        angle = (new_view - old_view) * 5
        sPointx, sPointy = Nrotate(math.radians(angle), cx, cy, img_w/2, img_h/2)
    if old_view > new_view:
        angle = (old_view - new_view) * 5
        sPointx, sPointy = Srotate(math.radians(angle), cx, cy, img_w/2, img_h/2)
    local_frame_h = int(img_h * 0.3)
    local_frame_w = int(img_w * 0.3)
    y_start = max((int(sPointy) - local_frame_h), 0)
    y_end = min((int(sPointy) + local_frame_h), 1080)
    x_start = max((int(sPointx) - local_frame_w), 0)
    x_end = min((int(sPointx) + local_frame_w), 1920)
    cv2.namedWindow('local', cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO)
    cv2.resizeWindow('local', 960, 720)
    cv2.imshow('local', frame)
    cv2.waitKey(0)
    local_frame = frame[int(y_start): int(y_end), int(x_start): int(x_end)]
    # cv2.namedWindow('local', cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO)
    # cv2.resizeWindow('local', 960, 720)
    cv2.imshow('local1', local_frame)
    cv2.waitKey(0)

    return new_view, local_frame, x_start, y_start


if __name__ == '__main__':
    imgsPath = './test/duoshidian/'
    imgslist = os.listdir(imgsPath)
    imgslist.sort(key=lambda x: int(x.split('-')[-2].split('-')[-1]))

    img1 = cv2.imread(imgsPath + imgslist[1])
    img2 = cv2.imread(imgsPath + imgslist[6])
    old_view = int(imgslist[0].split('-')[-2].split('-')[-1])
    new_view = int(imgslist[5].split('-')[-2].split('-')[-1])
    cx = 1000
    cy = 600
    cv2.namedWindow('current', cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO)
    cv2.resizeWindow('current', 960, 720)
    cv2.circle(img1, (cx, cy), 60, (255, 0, 0), 10)
    cv2.imshow('current', img1)
    cv2.waitKey(1)
    _, local_frame, x_start, y_start = dsd(cx, cy, old_view, new_view, img2)
    print(old_view)
    print(new_view)
    print(x_start)
    print(y_start)
