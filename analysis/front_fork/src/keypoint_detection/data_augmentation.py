# -*- coding: utf-8 -*-
"""
学習用画像のオーギュメンテーション処理
"""
import os
import cv2
import random
import common_image


def mk_450_600(img_list, org_dir, out_dir, insize_tuple, resize_tuple):
    for i, img in enumerate(img_list):
        im = cv2.imread(org_dir + img)
        if im is None:
            print img + 'の読み込みに失敗しました'
            continue
        resize_image = common_image.resize_image(im, resize_tuple)
        save_name = out_dir + img.replace('_' + str(insize_tuple[1]), '_' + str(resize_tuple[1])).replace('_' + str(insize_tuple[0]), '_' + str(resize_tuple[0]))
        common_image.save_image(resize_image, save_name)


def confirm_coordinate(coordinate_tuple, img):
    cv2.circle(img, (coordinate_tuple[0], coordinate_tuple[1]), 3, (0, 255, 0), -1)
    cv2.circle(img, (coordinate_tuple[2], coordinate_tuple[3]), 3, (0, 255, 0), -1)
    cv2.circle(img, (coordinate_tuple[4], coordinate_tuple[5]), 3, (0, 255, 0), -1)
    cv2.circle(img, (coordinate_tuple[6], coordinate_tuple[7]), 3, (0, 255, 0), -1)
    cv2.circle(img, (coordinate_tuple[8], coordinate_tuple[9]), 3, (0, 255, 0), -1)
    cv2.circle(img, (coordinate_tuple[10], coordinate_tuple[11]), 3, (0, 255, 0), -1)

    cv2.namedWindow('window')
    cv2.imshow('window', img)
    cv2.waitKey(0)


def resize_coordinate(coordinate_f, out_coordinate_f, out_dir_resize, insize_tuple, resize_tuple):
    with open(coordinate_f, 'r') as in_f:
        out_str = ''
        for line in in_f:
            values = line.rstrip().split('\t')
            processed = values[3]
            if processed != '1':
                continue

            out_list = []
            id = values[0]
            out_list.append(id)
            img_name = values[2].split('/')[-1]
            resize_name = img_name.replace('_' + str(insize_tuple[1]), '_' + str(resize_tuple[1])).replace('_' + str(insize_tuple[0]), '_' + str(resize_tuple[0]))
            img_path = out_dir_resize + resize_name
            out_list.append(img_path)

            # img_path = '../../data/resize_left/' + img_name
            point_ltx = float(values[4])
            point_lty = float(values[5])
            point_rtx = float(values[6])
            point_rty = float(values[7])
            point_lmx = float(values[8])
            point_lmy = float(values[9])
            point_rmx = float(values[10])
            point_rmy = float(values[11])
            point_lbx = float(values[12])
            point_lby = float(values[13])
            point_rbx = float(values[14])
            point_rby = float(values[15])

            w_rate = float(resize_tuple[0]) / float(insize_tuple[0])
            h_rate = float(resize_tuple[1]) / float(insize_tuple[1])

            out_ltx = point_ltx * w_rate
            out_lty = point_lty * h_rate
            out_rtx = point_rtx * w_rate
            out_rty = point_rty * h_rate
            out_lmx = point_lmx * w_rate
            out_lmy = point_lmy * h_rate
            out_rmx = point_rmx * w_rate
            out_rmy = point_rmy * h_rate
            out_lbx = point_lbx * w_rate
            out_lby = point_lby * h_rate
            out_rbx = point_rbx * w_rate
            out_rby = point_rby * h_rate
            out_list.append(str(out_ltx))
            out_list.append(str(out_lty))
            out_list.append(str(out_rtx))
            out_list.append(str(out_rty))
            out_list.append(str(out_lmx))
            out_list.append(str(out_lmy))
            out_list.append(str(out_rmx))
            out_list.append(str(out_rmy))
            out_list.append(str(out_lbx))
            out_list.append(str(out_lby))
            out_list.append(str(out_rbx))
            out_list.append(str(out_rby))

            out_str = out_str + ' '.join(out_list) + '\n'

        with open(out_coordinate_f, 'w') as out_f:
            out_f.write(out_str)


def create_clop_coordinate(out_coordinate_f, out_random_clop_dir, insize_tuple, resize_tuple, direction, aug_num):
    with open(out_coordinate_f, 'r')as in_f:
        out_str = ''
        for line in in_f:
            line = line.rstrip()
            values = line.split(' ')
            id = values[0]
            img_path = values[1]
            if not os.path.exists(img_path):
                continue
            point_ltx = float(values[2])
            point_lty = float(values[3])
            point_rtx = float(values[4])
            point_rty = float(values[5])
            point_lmx = float(values[6])
            point_lmy = float(values[7])
            point_rmx = float(values[8])
            point_rmy = float(values[9])
            point_lbx = float(values[10])
            point_lby = float(values[11])
            point_rbx = float(values[12])
            point_rby = float(values[13])

            img = cv2.imread(img_path)
            width = insize_tuple[0]
            height = insize_tuple[1]

            # 元の画像の1/2の大きさから乱数を発生させて、clopする範囲を指定。
            w_dist = random.randint(0, insize_tuple[0] / 2)
            h_dist = random.randint(0, insize_tuple[1] / 2)
            clop_img = img[h_dist:h_dist+height, w_dist:w_dist + width]
            # confirm_coordinate(clop_img)

            if direction == 'left':
                if point_ltx < w_dist:
                    point_ltx = -1
                else:
                    point_ltx = point_ltx - w_dist
                if point_rtx < w_dist:
                    point_rtx = -1
                else:
                    point_rtx = point_rtx - w_dist
                if point_lmx < w_dist:
                    point_lmx = -1
                else:
                    point_lmx = point_lmx - w_dist
                if point_rmx < w_dist:
                    point_rmx = -1
                else:
                    point_rmx = point_rmx - w_dist
                if point_lbx < w_dist:
                    point_lbx = -1
                else:
                    point_lbx = point_lbx - w_dist
                if point_rbx < w_dist:
                    point_rbx = -1
                else:
                    point_rbx = point_rbx - w_dist

                if point_lty < h_dist or (point_lty - h_dist > height):
                    point_lty = -1
                else:
                    point_lty = point_lty - h_dist
                if point_rty < h_dist or (point_rty - h_dist > height):
                    point_rty = -1
                else:
                    point_rty = point_rty - h_dist
                if point_lmy < h_dist or (point_lmy - h_dist > height):
                    point_lmy = -1
                else:
                    point_lmy = point_lmy - h_dist
                if point_rmy < h_dist or (point_rmy - h_dist > height):
                    point_rmy = -1
                else:
                    point_rmy = point_rmy - h_dist
                if (point_lby < h_dist) or (point_lby - h_dist > height):
                    point_lby = -1
                else:
                    point_lby = point_lby - h_dist
                if point_rby < h_dist or (point_rby - h_dist > height):
                    point_rby = -1
                else:
                    point_rby = point_rby - h_dist

            elif direction == 'right':
                if point_ltx > width + w_dist:
                    point_ltx = -1
                else:
                    point_ltx = point_ltx - w_dist
                if point_rtx > width + w_dist:
                    point_rtx = -1
                else:
                    point_rtx = point_rtx - w_dist
                if point_lmx > width + w_dist:
                    point_lmx = -1
                else:
                    point_lmx = point_lmx - w_dist
                if point_rmx > width + w_dist:
                    point_rmx = -1
                else:
                    point_rmx = point_rmx - w_dist
                if point_lbx > width + w_dist:
                    point_lbx = -1
                else:
                    point_lbx = point_lbx - w_dist
                if point_rbx > width + w_dist:
                    point_rbx = -1
                else:
                    point_rbx = point_rbx - w_dist

                if (point_lty - h_dist > height) or (point_lty - h_dist < 0):
                    point_lty = -1
                else:
                    point_lty = point_lty - h_dist
                if (point_rty - h_dist > height) or (point_rty - h_dist < 0):
                    point_rty = -1
                else:
                    point_rty = point_rty - h_dist
                if (point_lmy - h_dist > height) or (point_lmy - h_dist < 0):
                    point_lmy = -1
                else:
                    point_lmy = point_lmy - h_dist
                if (point_rmy - h_dist > height) or (point_rmy - h_dist < 0):
                    point_rmy = -1
                else:
                    point_rmy = point_rmy - h_dist
                if (point_lby - h_dist > height) or (point_lby - h_dist < 0):
                    point_lby = -1
                else:
                    point_lby = point_lby - h_dist
                if (point_rby - h_dist > height) or (point_rby - h_dist < 0):
                    point_rby = -1
                else:
                    point_rby = point_rby - h_dist

            if point_ltx != -1 and point_lty != -1 and point_rtx != -1 and point_rty != -1 and point_lmx != -1 and point_lmy != -1 and \
                point_rmx != -1 and point_rmy != -1 and point_lbx != -1 and point_lby != -1 and point_rbx != -1 and point_rby != -1 :
                print point_ltx, point_lty, point_rtx, point_rty, point_lmx, point_lmy , point_rmx, point_rmy, point_lbx, point_lby, point_rbx, point_rby

                coordinate_tuple = (point_ltx, point_lty, point_rtx, point_rty, point_lmx, point_lmy, point_rmx, point_rmy, point_lbx, point_lby, point_rbx, point_rby)

                save_name = str(aug_num) + '_' + values[1].split('/')[-1]\
                    .replace('_' + str(resize_tuple[0]), '_' + str(insize_tuple[0])).replace('_' + str(resize_tuple[1]),'_' + str(insize_tuple[1]))
                cv2.imwrite(out_random_clop_dir + save_name, clop_img)
                out_fname = out_random_clop_dir + save_name
                out_str = out_str + id + '_aug' + str(aug_num) + '\t' + 'aug' + '\t' + out_fname + '\t' + '1\t' + '\t'.join(map(str, coordinate_tuple)) + '\n'

    with open(out_dir_random_clop + 'right_random_coordinte_' + str(aug_num) + '.tsv' , 'w') as out_f:
        out_f.write(out_str)


def confirm_coordinate(result_file):
    with open(result_file, 'r') as in_f:
        for line in in_f:
            values = line.rstrip().split('\t')
            id = values[0]
            img_path = values[2]
            point_ltx = int(values[4].split('.')[0])
            point_lty = int(values[5].split('.')[0])
            point_rtx = int(values[6].split('.')[0])
            point_rty = int(values[7].split('.')[0])
            point_lmx = int(values[8].split('.')[0])
            point_lmy = int(values[9].split('.')[0])
            point_rmx = int(values[10].split('.')[0])
            point_rmy = int(values[11].split('.')[0])
            point_lbx = int(values[12].split('.')[0])
            point_lby = int(values[13].split('.')[0])
            point_rbx = int(values[14].split('.')[0])
            point_rby = int(values[15].split('.')[0])
            img = cv2.imread(img_path)

            # IDの追記
            cv2.putText(img,id,(320,30),cv2.FONT_HERSHEY_PLAIN, 2,(255, 255, 255))

            # 座標の追記
            cv2.circle(img, (point_ltx, point_lty), 3, (0, 255, 0), -1)
            cv2.circle(img, (point_rtx, point_rty), 3, (0, 255, 0), -1)
            cv2.circle(img, (point_lmx, point_lmy), 3, (0, 255, 0), -1)
            cv2.circle(img, (point_rmx, point_rmy), 3, (0, 255, 0), -1)
            cv2.circle(img, (point_lbx, point_lby), 3, (0, 255, 0), -1)
            cv2.circle(img, (point_rbx, point_rby), 3, (0, 255, 0), -1)
            cv2.namedWindow('window')
            cv2.imshow('window', img)
            cv2.waitKey(0)

if __name__ == '__main__':
    """
    target_image_dir：オーグメンテーション元の画像ディレクトリ
    insize_tuple：inputの画像サイズ(width, height)
    resize_tuple：リサイズするサイズ(width, height)
    adjust_rate；リサイズする割合(width, height)
    out_dir_resize：リサイズ後のカラーイメージ保存ディレクトリ
    db_result：MYSQLのDBダンプファイル
    out_coordinate_f：450 600のサイズにリサイズした座標ファイル(中間ファイル)
    out_dir_random_clop：ランダムにclopした画像の保存ディレクトリ
    dirction：左向きと右向きの方向の指定(left or right)
    """
    root_dir = '/usr/local/wk/git_local/bike/'
    target_image_dir = root_dir + 'analysis/front_fork/data/images/training_image/right_resize/'
    insize_tuple = (400, 300)
    resize_tuple = (600, 450)
    img_list = os.listdir(target_image_dir)
    # .DS_Storeの要素削除
    img_list = common_image.del_dsstore(img_list)
    out_dir_resize = root_dir + 'analysis/front_fork/data/augmentation/right/resize_right_450_600/'
    if not os.path.exists(out_dir_resize):
        os.mkdir(out_dir_resize)
    db_result = root_dir + 'analysis/front_fork/data/from_db/bike_result_20170412_right.tsv'
    out_coordinate_f = root_dir + 'analysis/front_fork/data/augmentation/right/right_bike_coordinate_450_600.tsv'
    out_dir_random_clop = root_dir + 'analysis/front_fork/data/augmentation/right/resize_random_clop_300_400/'
    if not os.path.exists(out_dir_random_clop):
        os.mkdir(out_dir_random_clop)
    direction = 'right'

    # 300 450から450 600を生成。
    # mk_450_600(img_list, target_image_dir, out_dir_resize, insize_tuple, resize_tuple)

    # 450 600画像の座標を生成
    # resize_coordinate(db_result, out_coordinate_f, out_dir_resize, insize_tuple, resize_tuple)

    # 450 600の画像を300 450でランダムにclopし、座標も修正
    for i in range(1, 10):
        create_clop_coordinate(out_coordinate_f, out_dir_random_clop, insize_tuple, resize_tuple, direction, i) # 第3引数はオーグメンテーションの回数

    # clopと座標の確認
    # result_file = '../data/bike_random_clop_coordinate.tsv'
    # confirm_coordinate(result_file)
