# -*- coding: utf-8 -*- 
import os
import sys
import numpy as np
import pandas as pd
import cv2


def convert_gray(result_path, img_path, gray_img_path, kubun):
    out_line = 'left_top_x,left_top_y,right_top_x,right_top_y,left_middle_x,left_middle_y,right_middle_x,right_middle_y,left_bottom_x,left_bottom_y,right_bottom_x,right_bottom_y,Image\n'
    with open(result_path, 'r') as f_result:
        for i, line in enumerate(f_result):
            line = line.rstrip()
            values = line.split('\t')
            img_id = values[0]
            img_data = values[2].split('/')[1]
            processed = values[3]
            left_top_x = values[4]
            left_top_y = values[5]
            right_top_x = values[6]
            right_top_y = values[7]
            left_middle_x = values[8]
            left_middle_y = values[9]
            right_middle_x = values[10]
            right_middle_y = values[11]
            left_bottom_x = values[12]
            left_bottom_y = values[13]
            right_bottom_x = values[14]
            right_bottom_y = values[15]

            if kubun == 'train':
                if processed == '1':
                    img = img_path + img_data
                    im = cv2.imread(img)
                    gray = cv2.cvtColor(im, cv2.COLOR_RGB2GRAY)
                    flat = gray.ravel()
                    flat_list = flat.tolist()
                    out_line = out_line +left_top_x + ',' + left_top_y + ',' + right_top_x + ',' + right_top_y + ',' + \
                               left_middle_x + ',' + left_middle_y + ',' + right_middle_x + ',' + right_middle_y + ',' + \
                               left_bottom_x + ',' + left_bottom_y + ',' + right_bottom_x + ',' + right_bottom_y + ',' + \
                               ' '.join(map(str,flat_list)) + '\n'
                    cv2.imwrite(gray_img_path + 'gray_' + img_data, gray)
                    print i
            elif kubun == 'test':
                if processed == '9':
                    img = img_path + img_data
                    im = cv2.imread(img)
                    gray = cv2.cvtColor(im, cv2.COLOR_RGB2GRAY)
                    flat = gray.ravel()
                    flat_list = flat.tolist()
                    out_line = out_line + img_id + ',' + ' '.join(map(str,flat_list)) + '\n'
                    cv2.imwrite(gray_img_path + 'gray_' + img_data, gray)
                    print i

    if kubun == 'train':
        out_f_name = '../data/bike_training_aug4.csv'
    elif kubun == 'test':
        out_f_name = '../data/bike_test.csv'

    with open(out_f_name, 'w') as f_out:
        f_out.write(out_line)

def create_gray_pixel(gray_img_path):
    file_list = os.listdir(gray_img_path)
    for img in file_list:
        im = cv2.imread(gray_img_path + img)

if __name__ == '__main__':
    root_path = '/usr/local/wk/git_local/bike/'
    img_path = root_path + 'tool/bike_make_tag/data/resize_random_clop_300_400/'
    gray_img_path = root_path + 'tool/bike_make_tag/data/resize_random_clop_left_gray/'
    if os.path.exists(gray_img_path) == False:
        os.mkdir(gray_img_path)
    result_path = root_path + '/tool/bike_make_tag/data/bike_random_clop_coordinate_4.tsv'
    convert_gray(result_path, img_path, gray_img_path, 'train')

    # create_gray_pixel(gray_img_path)