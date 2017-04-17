# -*- coding: utf-8 -*-
"""
画像パス、座標情報を持つcsvから、画像と座標をGUIで確認する。
"""
import numpy as np
import scipy as sc
import pandas as pd
import os
import sys
import cv2

def confirm_imshow(img):
    cv2.namedWindow('window')
    cv2.imshow('window', img)
    cv2.waitKey(0)

def confirm_coordinate(coordinate_file, split_char):
    with open(coordinate_file, 'r') as in_f:
        for line in in_f:
            values = line.rstrip().split(split_char)
            img_path = values[0]
            if img_path == 'left_top_x':
                continue

            point_ltx = int(values[1].split('.')[0])
            point_lty = int(values[2].split('.')[0])
            point_rtx = int(values[3].split('.')[0])
            point_rty = int(values[4].split('.')[0])
            point_lmx = int(values[5].split('.')[0])
            point_lmy = int(values[6].split('.')[0])
            point_rmx = int(values[7].split('.')[0])
            point_rmy = int(values[8].split('.')[0])
            point_lbx = int(values[9].split('.')[0])
            point_lby = int(values[10].split('.')[0])
            point_rbx = int(values[11].split('.')[0])
            point_rby = int(values[12].split('.')[0])
            img = cv2.imread(img_path)

            # 座標の追記
            cv2.circle(img, (point_ltx, point_lty), 3, (0, 255, 0), -1)
            cv2.circle(img, (point_rtx, point_rty), 3, (0, 255, 0), -1)
            cv2.circle(img, (point_lmx, point_lmy), 3, (0, 255, 0), -1)
            cv2.circle(img, (point_rmx, point_rmy), 3, (0, 255, 0), -1)
            cv2.circle(img, (point_lbx, point_lby), 3, (0, 255, 0), -1)
            cv2.circle(img, (point_rbx, point_rby), 3, (0, 255, 0), -1)
            print point_ltx,point_lty,point_rtx,point_rty,point_lmx,point_lmy,point_rmx,point_rmy,point_lbx,point_lby,point_rbx,point_rby
            confirm_imshow(img)


if __name__ == '__main__':
    coordinate_file = '/usr/local/wk/git_local/bike/analysis/front_fork/data/augmentation/right/resize_random_clop_300_400/right_random_coordinte_all_conf.tsv'
    split_char = '\t'
    confirm_coordinate(coordinate_file, split_char)
