# -*- coding: utf-8 -*-
"""
予測モデルを利用した座標予測
"""
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

        fig = plt.figure(figsize=(12, 6))
        ax = fig.add_subplot(1, 2, 1, xticks=[], yticks=[])
        plot_sample(sample1, y_pred1, ax)
        ax = fig.add_subplot(1, 2, 2, xticks=[], yticks=[])
        plot_sample(sample2, y_pred2, ax)
        plt.show()

def plot_sample(x, y_list, axis):
    img = x.reshape(300, 400)
    axis.imshow(img, cmap='gray')
    for i, coordinates in enumerate(y_list):
        if i == 0:   # left_bottom
            ops = ('x', 'b')
        elif i == 1: # left_middle
            ops = ('x', 'g')
        elif i == 2: # left_top
            ops = ('x', 'r')
        elif i == 3: # right_bottom
            ops = ('o', 'b')
        elif i == 4: # right_middle
            ops = ('o', 'g')
        elif i == 5: # right_top
            ops = ('o', 'r')

        axis.scatter(coordinates[:,0::2] * 200 + 200, coordinates[:,1::2] * 150 + 150, s=10, marker=ops[0], c=ops[1])
    #print y[:,0::2] = y[:,0::2] * 200 + 200
    #y[:,1::2] = y[:,1::2] * 150 + 150
    # axis.scatter(y[:,0::2] * 200 + 200, y[:,1::2] * 150 + 150, marker='x', s=10)

def drew_sample(model_dict, image_file):
    image_name = image_file.split('/')[-1]
    input_shape = (400, 300)
    X = dl.image_load2d(image_file, input_shape)
    y_predict_list = []

    for key in sorted(model_dict.keys()):
        print key
        # モデル読み込み
        model_architecture = model_dict[key].split(' ')[0]
        model_weight = model_dict[key].split(' ')[1]
        model = model_from_json(open(model_architecture).read())
        model.load_weights(model_weight)

        # 座標予測
        y_predict = model.predict(X)
        y_predict_list.append(y_predict)

    # 結果描写
    fig = plt.figure(figsize=(12, 6))
    ax = fig.add_subplot(1, 1, 1, xticks=[], yticks=[]) # subplot(行数, 列数, 何番目のプロットか)
    plot_sample(X, y_predict_list, ax)
    # 例表示
    plt.text(5, 10, "red:top, green:middle, blue:bottom",fontsize=12)
    plt.text(5, 30, "x:left, o:right",fontsize=12)

    plt.show()
    # plt.savefig('result/' + image_name.split('.')[0] + '.png')


"""
def drew_sample(model_dict, image_dir, dir):
    # モデル読み込み
    for key in sorted(model_dict.keys()):
        if key == 'left_bottom':
            lb_model_architecture = model_dict[key].split(' ')[0]
            lb_model_weight = model_dict[key].split(' ')[1]
            lb_model = model_from_json(open(lb_model_architecture).read())
            lb_model.load_weights(lb_model_weight)
        if key == 'left_middle':
            lm_model_architecture = model_dict[key].split(' ')[0]
            lm_model_weight = model_dict[key].split(' ')[1]
            lm_model = model_from_json(open(lm_model_architecture).read())
            lm_model.load_weights(lm_model_weight)
        if key == 'left_top':
            lt_model_architecture = model_dict[key].split(' ')[0]
            lt_model_weight = model_dict[key].split(' ')[1]
            lt_model = model_from_json(open(lt_model_architecture).read())
            lt_model.load_weights(lt_model_weight)
        if key == 'right_bottom':
            rb_model_architecture = model_dict[key].split(' ')[0]
            rb_model_weight = model_dict[key].split(' ')[1]
            rb_model = model_from_json(open(rb_model_architecture).read())
            rb_model.load_weights(rb_model_weight)
        if key == 'right_middle':
            rm_model_architecture = model_dict[key].split(' ')[0]
            rm_model_weight = model_dict[key].split(' ')[1]
            rm_model = model_from_json(open(rm_model_architecture).read())
            rm_model.load_weights(rm_model_weight)
        if key == 'right_top':
            rt_model_architecture = model_dict[key].split(' ')[0]
            rt_model_weight = model_dict[key].split(' ')[1]
            rt_model = model_from_json(open(rt_model_architecture).read())
            rt_model.load_weights(rt_model_weight)

    image_list = os.listdir(image_dir)

    for image_name in image_list:
        image_file = image_dir + image_name
        input_shape = (400, 300)
        X = dl.image_load2d(image_file, input_shape)
        y_predict_list = []

        # 座標予測
        lb_y_predict = lb_model.predict(X)
        lm_y_predict = lm_model.predict(X)
        lt_y_predict = lt_model.predict(X)
        rb_y_predict = rb_model.predict(X)
        rm_y_predict = rm_model.predict(X)
        rt_y_predict = rt_model.predict(X)
        y_predict_list.append(lb_y_predict)
        y_predict_list.append(lm_y_predict)
        y_predict_list.append(lt_y_predict)
        y_predict_list.append(rb_y_predict)
        y_predict_list.append(rm_y_predict)
        y_predict_list.append(rt_y_predict)

        # 結果描写
        fig = plt.figure(figsize=(12, 6))
        ax = fig.add_subplot(1, 1, 1, xticks=[], yticks=[]) # subplot(行数, 列数, 何番目のプロットか)
        plot_sample(X, y_predict_list, ax)
        # 例表示
        plt.text(5, 10, "red:top, green:middle, blue:bottom",fontsize=12)
        plt.text(5, 30, "x:left, o:right",fontsize=12)

        plt.show()
        # plt.savefig('result/' + image_name.split('.')[0] + '.png')
"""

if __name__ == '__main__':
    # 予測に利用するモデル指定
    model_dict = {}
    # point_list = ['right_top']
    point_list = ['left_top', 'left_middle', 'left_bottom', 'right_top', 'right_middle', 'right_bottom']

    for point in point_list:
        model_dict[point] = '../model/each/' + point + '/bike_conv_model_architecture_' + point + '.json ' + '../model/each/' + point + '/bike_conv_model_' + point + '_weights.h5'

    for key in model_dict:
        if not os.path.exists(model_dict[key].split(' ')[0]):
            print '[ERR]modelがない' + model_dict[key].split(' ')[0]
        if not os.path.exists(model_dict[key].split(' ')[1]):
            print '[ERR]modelがない' + model_dict[key].split(' ')[1]

    # テスト画像の読み込み
    image_file = '/usr/local/wk/git_local/bike/analysis/front_fork/data/ng_data/NG_LEFT.JPG'
    # image_file = '/usr/local/wk/git_local/bike/analysis/front_fork/data/training_image/resize_left/000220161109_l_300_400.jpg'
    # image_dir = '/usr/local/wk/git_local/bike/analysis/front_fork/data/ok_data/8500124B3016020100100_300_400.jpg'
    # image_dir = '/usr/local/wk/git_local/bike/analysis/front_fork/data/training_image/resize_random_clop_left_gray/'

    drew_sample(model_dict, image_file)

    # drew_sample(model_dict, image_dir, 'dir')



