# -*- coding: utf-8 -*-
"""
画像の共通処理
"""
import os
import cv2
import matplotlib.pyplot as plt

def resize_image(image, size_tuple):
    """
    :param image: cv2.imreadで読んだ画像配列[numpy.ndarray型]
    :param size_tuple: height , width のタプル型
    :return: リサイズしたnumpy.ndarray配列
    """
    resize_img = cv2.resize(image, size_tuple)
    return resize_img

def save_image(image, save_name):
    """
    :param image: cv2.imreadで読んだ画像配列[numpy.ndarray型]
    :param save_path: 保存するファイル名付きのパス
    :return: None
    """
    target_dir = save_name.replace(save_name.split('/')[-1], '')
    if not os.path.exists(target_dir):
        print 'create {0}'.format(target_dir)
        os.mkdir(target_dir)
    cv2.imwrite(save_name, image)

def gray_convert(image):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    return gray

def image_show(image):
    cv2.imshow('test', image)
    cv2.waitKey(0)             # キーウェイト無制限
    cv2.destroyAllWindows()    # 作成したウインドウの破棄
