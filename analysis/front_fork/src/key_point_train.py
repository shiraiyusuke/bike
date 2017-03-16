# -*- coding: utf-8 -*-
import os
import numpy as np
from pandas.io.parsers import read_csv
from sklearn.utils import shuffle
from sklearn.cross_validation import train_test_split

from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.optimizers import SGD
from keras.models import model_from_json
from keras.layers import Convolution2D, MaxPooling2D, Flatten, Dropout
from keras.utils.visualize_util import plot
from keras.preprocessing.image import ImageDataGenerator
from keras.callbacks import LearningRateScheduler

from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.layers.convolutional import Convolution2D, MaxPooling2D
from keras.layers.normalization import BatchNormalization
from keras.regularizers import l2


import matplotlib.pyplot as plt

FTRAIN = '../data/bike_training.csv'
FTEST = '../data/bike_test_ng.csv'


def make_conv_model():
    X, y = load2d()
    model2 = Sequential()

    # model2.add(Convolution2D(32, 3, 3, input_shape=(1, 96, 96))) # こっちだと上手くいかなかった(by theano)
    # model2.add(Convolution2D(32, 3, 3, input_shape=(96, 96, 1)))
    model2.add(Convolution2D(32, 3, 3, input_shape=(300, 400, 1)))
    model2.add(Activation('relu'))
    model2.add(MaxPooling2D(pool_size=(2, 2)))

    model2.add(Convolution2D(64, 2, 2))
    model2.add(Activation('relu'))
    model2.add(MaxPooling2D(pool_size=(2, 2)))

    model2.add(Convolution2D(128, 2, 2))
    model2.add(Activation('relu'))
    model2.add(MaxPooling2D(pool_size=(2, 2)))

    model2.add(Flatten())
    model2.add(Dense(500))
    model2.add(Activation('relu'))
    model2.add(Dense(500))
    model2.add(Activation('relu'))
    model2.add(Dense(12))

    sgd = SGD(lr=0.01, momentum=0.9, nesterov=True)
    model2.compile(loss='mean_squared_error', optimizer=sgd)
    hist2 = model2.fit(X, y, nb_epoch=1000, validation_split=0.2)

    json_string = model2.to_json()
    open('../model/bike_conv_model_architecture.json', 'w').write(json_string)
    model2.save_weights('../model/bike_conv_model_weights.h5')


def make_conv_model3():
    X, y = load2d()
    model3 = Sequential()
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

    # model2.add(Convolution2D(32, 3, 3, input_shape=(1, 96, 96))) # こっちだと上手くいかなかった(by theano)
    # model2.add(Convolution2D(32, 3, 3, input_shape=(96, 96, 1)))
    model3.add(Convolution2D(32, 3, 3, input_shape=(300, 400, 1)))
    model3.add(Activation('relu'))
    model3.add(MaxPooling2D(pool_size=(2, 2)))
    model3.add(Dropout(0.1))

    model3.add(Convolution2D(64, 2, 2))
    model3.add(Activation('relu'))
    model3.add(MaxPooling2D(pool_size=(2, 2)))
    model3.add(Dropout(0.2))

    model3.add(Convolution2D(128, 2, 2))
    model3.add(Activation('relu'))
    model3.add(MaxPooling2D(pool_size=(2, 2)))
    model3.add(Dropout(0.3))

    model3.add(Flatten())
    model3.add(Dense(1000))
    model3.add(Activation('relu'))
    model3.add(Dropout(0.5))
    model3.add(Dense(1000))
    model3.add(Activation('relu'))
    model3.add(Dense(12))

    start = 0.03
    stop = 0.001
    nb_epoch = 30
    learning_rates = np.linspace(start, stop, nb_epoch)

    change_lr = LearningRateScheduler(lambda epoch: float(learning_rates[epoch]))
    sgd = SGD(lr=0.01, momentum=0.9, nesterov=True, decay=1e-6)
    model3.compile(loss='mean_squared_error', optimizer=sgd)
    hist3 = model3.fit(X, y, nb_epoch=1000, validation_split=0.2)

    json_string = model3.to_json()
    open('../model/bike_conv_model3_architecture.json', 'w').write(json_string)
    model3.save_weights('../model/bike_conv_model3_weights.h5')


def drew_sample(model1, model2):
    # sampleの[1:2]を変えるとサンプルが変化
    for i in range(42):
        sample1 = load2d(test=True)[0][i:i+1]
        sample2 = load2d(test=True)[0][i:i+1]
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

def make_simple_model(model_architecture='', model_weight=''):
    if model_weight == '':
        X, y = load()
        print("X.shape == {}; X.min == {:.3f}; X.max == {:.3f}".format(X.shape, X.min(), X.max()))
        print("y.shape == {}; y.min == {:.3f}; y.max == {:.3f}".format(y.shape, y.min(), y.max()))

        model = Sequential()
        model.add(Dense(100, input_dim=120000))
        model.add(Activation('relu'))
        model.add(Dense(12))

        sgd = SGD(lr=0.05, momentum=0.9, nesterov=True) # Nesterov accelerated gradient[NAG]を利用
        model.compile(loss='mean_squared_error', optimizer=sgd)
        hist = model.fit(X, y, nb_epoch=30, validation_split=0.2) # validation_split=0.2でサンプルのうち20%をバリデーションに。

        json_string = model.to_json()
        open('../model/bike_model1_architecture_5.json', 'w').write(json_string)
        model.save_weights('../model/bike_model1_weights_5.h5')

        plt.plot(hist.history['loss'], linewidth=3, label='train')
        plt.plot(hist.history['val_loss'], linewidth=3, label='valid')
        plt.grid()
        plt.legend()
        plt.xlabel('epoch')
        plt.ylabel('loss')
        plt.yscale('log')
        plt.show()


    elif model_architecture != '':
        # モデルの読み込み
        model = model_from_json(open(model_architecture).read())
        model.load_weights(model_weight)

    X_test, _ = load(test=True)
    y_test = model.predict(X_test)

    fig = plt.figure(figsize=(6, 6))
    fig.subplots_adjust(
        left=0, right=1, bottom=0, top=1, hspace=0.05, wspace=0.05)

    for i in range(16):
        axis = fig.add_subplot(4, 4, i+1, xticks=[], yticks=[])
        print(y_test[i])
        plot_sample(X_test[i], y_test[i], axis)

    plt.show()

def load(test=False, cols=None):
    fname = FTEST if test else FTRAIN
    df = read_csv(os.path.expanduser(fname))
    # print(df.head())

    # グレースケールのピクセル値をnumpyのarrayに変換
    df['Image'] = df['Image'].apply(lambda im: np.fromstring(im, sep =' '))

    if cols:
        df = df[list(cols) + ['Image']]

    print(df.count())
    df = df.dropna()

    X = np.vstack(df['Image'].values) / 255. # 0〜1の値に変換
    X = X.astype(np.float32)

    if not test:
        y = df[df.columns[:-1]].values # 最後のカラム[Image]以外(正解ラベル)を取得。
        # y = df[df.columns[0:10]].values # 正解のデータ個数を変えたければ
        y = (y - 48) / 48
        X, y = shuffle(X, y, random_state=42) # データをシャッフル
        y = y.astype(np.float32)
    else:
        y = None

    return X, y


def load2d(test=False, cols=None):
    X, y = load(test, cols)
    # X = X.reshape(-1, 1, 96, 96)
    # X = X.reshape(-1, 1, 300, 400)
    # X = X.reshape(-1, 96, 96, 1)
    X = X.reshape(-1, 300, 400, 1)
    return X, y




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

