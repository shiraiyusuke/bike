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

def resize_coordinate(coordinate_tuple, size_tuple):
    """座標情報を指定したスケールで修正
    :param coordinate_tuple:
    :param size_tuple:
    :return:
    """
    x = coordinate_tuple[0]
    y = coordinate_tuple[1]
    w_rate = size_tuple[0]
    h_rate = size_tuple[1]
    x = float(x) * w_rate
    y = float(y) * h_rate
    return (x, y)

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

def del_dsstore(inlist):
    if '.DS_Store' in inlist:
        inlist.remove('.DS_Store')
    return inlist

def make_training_data_from_gray_image(coordinate_list, gray_image, out_training_csv, save_gray_image_name):
    """
    以下を利用して、学習用のcsvを作成する。
    :param coordinate_list: 座標情報のリスト(中身はxとy座標のタプル)
    :param gray_image: grayscaleのイメージのnp.arrayデータ
    :param out_training_csv: 出力ファイル
    :param save_gray_image_name: グレースケール画像の保存先ディレクトリ
    :return: None
    """
    with open(out_training_csv, 'a') as out_f:
        out_list =[]
        out_list.append(save_gray_image_name)
        for i in range(len(coordinate_list)):
            out_list.append(coordinate_list[i][0])
            out_list.append(coordinate_list[i][1])
        flat = gray_image.ravel()
        flat_list = flat.tolist()

        out_f.write(','.join(map(str, out_list)) + ',' + ' '.join(map(str,flat_list)) + '\n')
