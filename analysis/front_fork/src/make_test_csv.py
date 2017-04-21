# -*- coding: utf-8 -*-
import numpy as np
import scipy as sc
import pandas as pd
import os
import sys
import cv2
import common_image


def make_test_csv(test_image_path, out_f):
    img_list = [x for x in os.listdir(test_image_path) if '.JPG' in x]
    out_line = 'Image_id,Image\n'
    for i, img_name in enumerate(img_list):
        img_id = i + 1
        image = test_image_path + img_name
        img = cv2.imread(image)
        resize = (400, 300)
        resize_image = common_image.resize_image(img, resize)
        gray = cv2.cvtColor(resize_image, cv2.COLOR_RGB2GRAY)
        common_image.save_image(gray, test_image_path + 'gray/' + img_name)
        print gray.shape
        flat = gray.ravel()
        flat_list = flat.tolist()
        out_line = out_line + str(img_id) + ',' + ' '.join(map(str,flat_list)) + '\n'
        # cv2.imwrite(gray_img_path + 'gray_' + img_data, gray)
        print i
    with open(out_f, 'w') as out_file:
        out_file.write(out_line)


def check_num(out_f):
    with open(out_f, 'r') as in_f:
        for line in in_f:
            val = line.split(',')
            if len(val) != 2:
                print ',区切りの数が違う'
            pixel = val[1].split(' ')
            if len(pixel) != 300 * 400:
                print 'グレースケールのピクセル数が違う{0:d}'.format(len(pixel))


if __name__ == '__main__':
    root_path = '/usr/local/wk/git_local/bike/'
    data_path = root_path + '/analysis/front_fork/data/'
    test_image_path = data_path + 'ng_data/'
    out_f = data_path + 'bike_test_ng.csv'
    make_test_csv(test_image_path, out_f)
    # check_num(out_f)
