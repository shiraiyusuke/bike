# -*- coding: utf-8 -*-
import os
import numpy as np
from pandas.io.parsers import read_csv
from sklearn.utils import shuffle
import cv2
import common_image as ci

FTRAIN = '../data/bike_training.csv'
FTEST = '../data/bike_test_ng.csv'


def load(test=False, cols=None):
    fname = FTEST if test else FTRAIN
    df = read_csv(os.path.expanduser(fname))
    # グレースケールのピクセル値をnumpyのarrayに変換
    df['Image'] = df['Image'].apply(lambda im: np.fromstring(im, sep =' '))

    if cols:
        df = df[list(cols) + ['Image']]

    df = df.dropna()
    X = np.vstack(df['Image'].values) / 255. # 0〜1の値に変換
    X = X.astype(np.float32)

    if not test:
        y = df[df.columns[:-1]].values.astype(np.float32) # 最後のカラム[Image]以外(正解ラベル)を取得。
        # 奇数番目(横のサイズ)を正規化
        y[:,0::2] = (y[:,0::2] - 200.) / 200.
        # 偶数番目(縦のサイズ)を正規化
        y[:,1::2] = (y[:,1::2] - 150.) / 150.
        # y = (y - 48) / 48
        X, y = shuffle(X, y, random_state=42) # データをシャッフル
        y = y.astype(np.float32)
    else:
        y = None

    return X, y


def load2d(test=False, cols=None, shape=(), backend='tensorflow'):
    """

    :param test: train用かtest用かのflg
    :param cols:
    :param shape: リサイズのheight, weightのタプル
    :param backend: tensorflow or theano
    :return: X:imageのNdarray, y:ラベルのリスト
    """
    X, y = load(test, cols)
    if backend == 'tensorflow':
        X = X.reshape(-1, shape[0], shape[1], 1)
    elif backend == 'theano':
        X = X.reshape(-1, shape[0], shape[1], 1)
    return X, y

def image_load2d(img_name, shape, backend, out_dir_gray):
    image = cv2.imread(img_name)
    resize_image = ci.resize_image(image, shape)
    gray_image = ci.gray_convert(resize_image)
    out_name = out_dir_gray + img_name.split('/')[-1]
    ci.save_image(gray_image, out_name)

    X = gray_image
    #X = gray_image.ravel()
    X = X / 255. # 正規化
    X = X.astype(np.float32)

    if backend == 'tensor':
        X = X.reshape(-1, 300, 400, 1)
    elif backend == 'theano':
        X = X.reshape(-1, 300, 400, 1)
    return X
