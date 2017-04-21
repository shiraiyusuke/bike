# -*- coding: utf-8 -*-
"""
学習用データの作成処理
"""
import os
import sys
import numpy as np
import pandas as pd
import cv2


def convert_gray(result_path, img_path, gray_img_path, data_kubun, source_kubun):
    if data_kubun == 'train':
        out_f_name = '../data/bike_training.csv'
    elif data_kubun == 'test':
        out_f_name = '../data/bike_test.csv'

    with open(result_path, 'r') as f_result:

        with open(out_f_name, 'a') as f_out:
            out_line = 'left_top_x,left_top_y,right_top_x,right_top_y,left_middle_x,left_middle_y,right_middle_x,right_middle_y,left_bottom_x,left_bottom_y,right_bottom_x,right_bottom_y,Image\n'
            f_out.write(out_line)

            for i, line in enumerate(f_result):
                line = line.rstrip()
                if source_kubun == 'db':
                    split_char = ' '
                else:
                    split_char = '\t'
                values = line.split(split_char)
                processed = values[3]
                if processed != '1':
                    continue
                img_id = values[0]
                img_data = values[2].split('/')[-1]
                left_top_x = values[4].split('.')[0]
                left_top_y = values[5].split('.')[0]
                right_top_x = values[6].split('.')[0]
                right_top_y = values[7].split('.')[0]
                left_middle_x = values[8].split('.')[0]
                left_middle_y = values[9].split('.')[0]
                right_middle_x = values[10].split('.')[0]
                right_middle_y = values[11].split('.')[0]
                left_bottom_x = values[12].split('.')[0]
                left_bottom_y = values[13].split('.')[0]
                right_bottom_x = values[14].split('.')[0]
                right_bottom_y = values[15].split('.')[0]

                if data_kubun == 'train':
                    if processed == '1':
                        img = img_path + img_data
                        im = cv2.imread(img)
                        gray = cv2.cvtColor(im, cv2.COLOR_RGB2GRAY)
                        flat = gray.ravel()
                        flat_list = flat.tolist()
                        out_line = left_top_x + ',' + left_top_y + ',' + right_top_x + ',' + right_top_y + ',' + \
                                   left_middle_x + ',' + left_middle_y + ',' + right_middle_x + ',' + right_middle_y + ',' + \
                                   left_bottom_x + ',' + left_bottom_y + ',' + right_bottom_x + ',' + right_bottom_y + ',' + \
                                   ' '.join(map(str,flat_list)) + '\n'
                        f_out.write(out_line)

                        # cv2.imwrite(gray_img_path + 'gray_' + img_data, gray)
                        print i
                elif data_kubun == 'test':
                    if processed == '9':
                        img = img_path + img_data
                        im = cv2.imread(img)
                        gray = cv2.cvtColor(im, cv2.COLOR_RGB2GRAY)
                        flat = gray.ravel()
                        flat_list = flat.tolist()
                        out_line = out_line + img_id + ',' + ' '.join(map(str,flat_list)) + '\n'
                        cv2.imwrite(gray_img_path + 'gray_' + img_data, gray)
                        print i



def create_gray_pixel(gray_img_path):
    file_list = os.listdir(gray_img_path)
    for img in file_list:
        im = cv2.imread(gray_img_path + img)

if __name__ == '__main__':
    root_path = '/usr/local/wk/git_local/bike/'
    img_path = root_path + 'analysis/front_fork/data/training_image/resize_left/'
    # img_path = root_path + 'analysis/front_fork/data/training_image/resize_random_clop_300_400/'
    gray_img_path = root_path + 'analysis/front_fork/data/training_image/resize_left_gray/'
    if os.path.exists(gray_img_path) == False:
        os.mkdir(gray_img_path)
    # result_path = root_path + 'analysis/front_fork/data/bike_random_clop_coordinate.tsv'
    result_path = root_path + 'analysis/front_fork/data/left_bike_coordinate_20170318.tsv'
    convert_gray(result_path, img_path, gray_img_path, 'train', 'db')

    # create_gray_pixel(gray_img_path)