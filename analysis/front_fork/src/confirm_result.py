# -*- coding: utf-8 -*-
import os
from keras.models import model_from_json
import matplotlib.pyplot as plt
import key_point_train
import data_load as dl
import cv2

FTRAIN = '../data/bike_training.csv'
FTEST = '../data/bike_test_ng.csv'


def drew_sample(model1, model2):
    # sampleの[1:2]を変えるとサンプルが変化
    for i in range(42):
        sample1 = key_point_train.load2d(test=True)[0][i:i + 1]
        sample2 = key_point_train.load2d(test=True)[0][i:i + 1]
        y_pred1 = model1.predict(sample1)[0]
        y_pred2 = model2.predict(sample2)[0]
        print y_pred2

        fig = plt.figure(figsize=(12, 6))
        ax = fig.add_subplot(1, 2, 1, xticks=[], yticks=[])
        plot_sample(sample1, y_pred1, ax)
        ax = fig.add_subplot(1, 2, 2, xticks=[], yticks=[])
        plot_sample(sample2, y_pred2, ax)
        plt.show()

def plot_sample(x, y, axis):
    print y
    img = x.reshape(300, 400)
    axis.imshow(img, cmap='gray')
    #print y[:,0::2] = y[:,0::2] * 200 + 200
    #y[:,1::2] = y[:,1::2] * 150 + 150
    axis.scatter(y[:,0::2] * 200 + 200, y[:,1::2] * 150 + 150, marker='x', s=10)

def drew_sample(model_dict):
    for key in model_dict:
        # モデル読み込み
        model_architecture = model_dict[key].split(' ')[0]
        model_weight = model_dict[key].split(' ')[1]
        model = model_from_json(open(model_architecture).read())
        model.load_weights(model_weight)

        # テスト用画像の読み込み
        image_file = '/usr/local/wk/git_local/bike/tool/bike_make_tag/data/resize_random_clop_left_gray/gray_2_021420160309_l_300_400.jpg'
        input_shape = (400, 300)
        X = dl.image_load2d(image_file, input_shape)

        # 座標予測
        y_pred = model.predict(X)
        # y_pred = model.predict(X_img)
        print y_pred

        # 結果描写
        fig = plt.figure(figsize=(12, 6))
        ax = fig.add_subplot(1, 1, 1, xticks=[], yticks=[]) # subplot(行数, 列数, 何番目のプロットか)
        plot_sample(X, y_pred, ax)

        # plot_sample(X, y_pred, ax)
        plt.show()
        print 'end'



if __name__ == '__main__':
    # 予測に利用するモデル指定
    model_dict = {}
    point_list = ['right_bottom']
    # point_list = ['left_top', 'left_middle', 'left_bottom', 'right_top', 'right_middle', 'right_bottom']

    for point in point_list:
        model_dict[point] = '../model/each/' + point + '/bike_conv_model3_architecture_' + point + '.json ' + '../model/each/' + point + '/bike_conv_model3_' + point + '_weights.h5'

    for key in model_dict:
        if not os.path.exists(model_dict[key].split(' ')[0]):
            print '[ERR]modelがない' + model_dict[key].split(' ')[0]
        if not os.path.exists(model_dict[key].split(' ')[1]):
            print '[ERR]modelがない' + model_dict[key].split(' ')[1]

    # 1サンプルの描画
    drew_sample(model_dict)

