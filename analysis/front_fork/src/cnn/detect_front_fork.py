# -*- coding: utf-8 -*-
import cv2
import os
import numpy as np
import common_image


def detect_front_fork(cascade_file, image_dir):
    Cascadefile = cv2.CascadeClassifier(cascade_file)
    image_list = os.listdir(image_dir)
    image_list = common_image.del_dsstore(image_list)
    for line in image_list:
        image_file = image_dir + line
        print image_file
        image = cv2.imread(image_file, cv2.IMREAD_COLOR)
        if image is None:
            print 'image is not find'

        img = common_image.resize_image(image, (400,300))
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        coordinate = Cascadefile.detectMultiScale(gray, scaleFactor=1.09, minNeighbors=30, minSize=(40, 40))
        # minNeighborsを上げれば検出される数が減る。 scaleFactorを上げると検出される数が減る。
        print coordinate

        if len(coordinate) > 0:
            for rect in coordinate:
                cv2.rectangle(img, tuple(rect[0:2]), tuple(rect[0:2]+rect[2:4]), (0, 0,255), thickness=2)
        else:
            print "no detect"

        cv2.namedWindow('window')
        cv2.imshow('window', img)
        cv2.waitKey(0)


if __name__ == '__main__':
    """
    カスケード検出器を用いて、フロントフォークの座標を特定する。
    dirction: 対象の方向
    cascade_file: 学習済みのカスケードファイル
    img: 予測対象画像ファイルパス
    """
    root_dir = '/usr/local/wk/git_local/bike/'
    direction = 'right'
    cascade_file = root_dir + 'analysis/front_fork/data/cascade/' + direction + '/model/4/cascade.xml'
    # image_file = root_dir + 'analysis/front_fork/data/images/right/test_image/ok_data/4e4baa8f35.jpg'
    image_dir = '/usr/local/wk/git_local/bike/analysis/front_fork/data/cascade/right/images/test/'
    detect_front_fork(cascade_file, image_dir)
