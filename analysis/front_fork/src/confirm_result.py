# -*- coding: utf-8 -*-
import os
from pandas.io.parsers import read_csv
from keras.models import model_from_json
import matplotlib.pyplot as plt
import bike_key_point_train

FTRAIN = '../data/bike_training.csv'
FTEST = '../data/bike_test_ng.csv'


def drew_sample(model1, model2):
    # sampleの[1:2]を変えるとサンプルが変化
    for i in range(42):
        sample1 = bike_key_point_train.load2d(test=True)[0][i:i+1]
        sample2 = bike_key_point_train.load2d(test=True)[0][i:i+1]
        y_pred1 = model1.predict(sample1)[0]
        y_pred2 = model2.predict(sample2)[0]
        print y_pred2

        fig = plt.figure(figsize=(12, 6))
        ax = fig.add_subplot(1, 2, 1, xticks=[], yticks=[])
        plot_sample(sample1, y_pred1, ax)
        ax = fig.add_subplot(1, 2, 2, xticks=[], yticks=[])
        plot_sample(sample2, y_pred2, ax)
        plt.show()

    """
    sample1 = load(test=True)[0][7:8]  #[7:8]を変えるとサンプルが変化する。
    sample2 = load2d(test=True)[0][9:10]
    y_pred1 = model1.predict(sample1)[0]
    y_pred2 = model2.predict(sample2)[0]
    print y_pred2

    fig = plt.figure(figsize=(6, 3))
    ax = fig.add_subplot(1, 2, 1, xticks=[], yticks=[])
    plot_sample(sample1, y_pred1, ax)
    ax = fig.add_subplot(1, 2, 2, xticks=[], yticks=[])
    plot_sample(sample2, y_pred2, ax)
    plt.show()
    """

def data_augmentation():
    # 画像の反転
    X, y = load2d()
    X_flipped = X[:, :, ::-1, :] # 左右反転
    # X_flipped = X[:, :, :, ::-1]
    # X_flipped = X[:, ::-1, :, :] # 上下反転

    fig = plt.figure(figsize=(6, 3))
    ax = fig.add_subplot(1, 2, 1, xticks=[], yticks=[])
    plot_sample(X[1], y[1], ax)
    ax = fig.add_subplot(1, 2, 2, xticks=[], yticks=[])
    plot_sample(X_flipped[1], y[1], ax)
    plt.show()

    # keypointの反転
    flip_indices = [
        (0, 2), (1, 3),
        (4, 8), (5, 9), (6, 10), (7, 11),
        (12, 16), (13, 17), (14, 18), (15, 19),
        (22, 24), (23, 25),
        ]

    df = read_csv(os.path.expanduser(FTRAIN))
    for i, j in flip_indices:
        print("{} -> {}".format(df.columns[i], df.columns[j]))


def plot_sample(x, y, axis):
    img = x.reshape(300, 400)
    axis.imshow(img, cmap='gray')
    axis.scatter(y[0::2] * 48 + 48, y[1::2] * 48 + 48, marker='x', s=10)






if __name__ == '__main__':
    model1_architecture = '../model/bike_model1_architecture_5.json'
    model1_weight = '../model/bike_model1_weights_5.h5'
    # make_simple_model(model1_architecture, model1_weight)
    # make_simple_model()

    conv_model1_architecture = '../model/bike_conv_model_architecture_arg_8.json'
    conv_model1_weight = '../model/bike_conv_model_weights_arg_8.h5'

    conv_model2_architecture = '../model/bike_conv_model_architecture_arg.json'
    conv_model2_weight = '../model/bike_conv_model_weights_arg.h5'

    # make_conv_model()
    # make_conv_model3()

    # モデルの読み込み
    model1 = model_from_json(open(conv_model1_architecture).read())
    model1.load_weights(conv_model1_weight)
    model2 = model_from_json(open(conv_model2_architecture).read())
    model2.load_weights(conv_model2_weight)
    #model2 = model_from_json(open(model2_architecture).read())
    #model2.load_weights(model2_weight)

    # ネットワーク描写
    # plot(conv_model1, to_file='model2.png', show_shapes=True)

    # 1サンプルの描画
    drew_sample(model1, model2)

    # データオーグメンテーション
    # data_augmentation()

    # X, y = load2d()
    # X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

    # start = 0.03
    # stop = 0.001
    # nb_epoch = 5000
    # learning_rates = np.linspace(start, stop, nb_epoch)

