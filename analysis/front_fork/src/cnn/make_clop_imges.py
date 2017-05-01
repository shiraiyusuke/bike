# -*- coding: utf-8 -*-
import cv2
import os
import common_image
import random
import numpy as np


def make_negative_file(direction, out_positive_file, out_negative_file, out_negative_image_dir, input_size):
    with open(out_positive_file, 'r') as posf:
        for line in posf:
            values = line.rstrip().split(' ')
            image_path = values[0]
            x = values[2]
            y = values[3]
            w = values[4]
            h = values[5]
            if direction == 'right':
                w = np.random.normal(100, 15)
                h = np.random.normal(150, 20)
                if int(float(x)) - w < 0:
                    continue
                for i in range(2): # 1枚につき2枚のnegativeを生成
                    x_neg = random.randint(0, int(float(x)) - int(w))
                    y_neg = random.randint(0, int(input_size[1]) - int(h))
                    image = cv2.imread(image_path)
                    neg_image = common_image.clop_image(image, x_neg, y_neg, w, h)
                    save_nega_name = out_negative_image_dir + 'neg_' + str(i) + '_' + image_path.split('/')[-1]
                    common_image.save_image(neg_image, save_nega_name)
                    with open(out_negative_file, 'a') as negf:
                        negf.write(save_nega_name + '\n')


def make_clop_image(out_positive_file, out_clop_image_dir):
    with open(out_positive_file, 'r') as coordf:
        for line in coordf:
            values = line.rstrip().split(' ')
            image_path = values[0]
            x = float(values[2])
            y = float(values[3])
            w = float(values[4])
            h = float(values[5])
            if not os.path.exists(image_path):
                print '%s is not exist' % (image_path)
                continue
            image = cv2.imread(image_path)
            clop_image = common_image.clop_image(image, x, y, w, h)
            save_name = out_clop_image_dir + 'forkclop_' + image_path.split('/')[-1]
            common_image.save_image(clop_image, save_name)


def make_positive_file(in_db_file, input_size, out_positive_file, target_dir):
    if os.path.exists(out_positive_file):
        os.remove(out_positive_file)

    with open(in_db_file, 'r') as inf:
        for line in inf:
            out_list = []
            values = line.rstrip().split('\t')

            id = values[0]
            if id == 'image_id': continue

            image_name = values[2].split('/')[-1]

            processed = values[3]
            if not processed != 1: continue

            ltx = float(values[4])
            lty = float(values[5])
            rtx = float(values[6])
            rty = float(values[7])
            lmx = float(values[8])
            lmy = float(values[9])
            rmx = float(values[10])
            rmy = float(values[11])
            lbx = float(values[12])
            lby = float(values[13])
            rbx = float(values[14])
            rby = float(values[15])

            xlist = [ltx, rtx, lmx, rmx, lbx, rbx]
            ylist = [lty, rty, lmy, rmy, lby, rby]
            xmax, xmin = max(xlist), min(xlist)
            ymax, ymin = max(ylist), min(ylist)

            xmin = xmin - 20.0 if xmin - 20.0 > 0 else xmin
            xmax = xmax + 20.0 if xmax + 20.0 < float(input_size[0]) else xmax
            ymin = ymin - 20.0 if ymin - 20.0 > 0 else ymin
            ymax = ymax + 20.0 if ymax + 20.0 < float(input_size[1]) else ymax

            out_list.append(image_name)
            out_list.append(xmin)
            out_list.append(xmax)
            out_list.append(ymin)
            out_list.append(ymax)
            with open(out_positive_file, 'a') as positive:
                positive.write(' '.join([target_dir + image_name, str(1), str(xmin), str(ymin), str(xmax - xmin), str(ymax - ymin)]) + '\n')

if __name__ == '__main__':
    """
    カスケード検出器にかけるためのdatファイルを作成する。
    その際、学習用の確認画像も出力する。
    direction: 対象の向き[left or right]
    in_db_file: MySQLのダンプファイル
    target_dir:　元となる画像ディレクトリ
    input_size: 元の画像のサイズ(width, height)
    out_square_file: フォークの座標ファイル
    out_clop_image_dir: フォークの画像保存用ディレクトリ
    out_positive_file: カスケード検出器用のpositive.datファイル
    out_negative_file: カスケード検出器用のnegative.datファイル
    out_negative_image_dir: negative.datの画像ディレクトリ
    """
    root_dir = '/usr/local/wk/git_local/bike/'
    direction = 'right'
    in_db_file = root_dir + 'analysis/front_fork/data/from_db/' + direction + '/front_fork_' + direction + '.tsv'
    target_dir = root_dir + 'analysis/front_fork/data/images/' + direction + '/training_image/' + direction + '_resize/'
    input_size = (400, 300)
    out_clop_image_dir = root_dir + 'analysis/front_fork/data/cascade/' + direction + '/images/color/'
    if not os.path.exists(out_clop_image_dir):
        os.mkdir(out_clop_image_dir)

    out_positive_file = root_dir + '/analysis/front_fork/data/cascade/' + direction + '/datfile/positive_' + direction + '.dat'
    out_negative_file = root_dir + '/analysis/front_fork/data/cascade/' + direction + '/datfile/negative_' + direction + '.dat'
    out_negative_image_dir = root_dir + '/analysis/front_fork/data/cascade/' + direction + '/images/negative/'

    # positive.dat作成
    # make_positive_file(in_db_file, input_size, out_positive_file, target_dir)
    # フォークのみの画像作成
    # make_clop_image(out_positive_file, out_clop_image_dir)

    # negative.dat作成と画像作成
    make_negative_file(direction, out_positive_file, out_negative_file, out_negative_image_dir, input_size)

