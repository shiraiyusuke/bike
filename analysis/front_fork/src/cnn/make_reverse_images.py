# -*- coding: utf-8 -*-

import common_image
import cv2
import os


def main():
    """
    対象のディレクトリの画像を反転させる
    target_dir: 対象のディレクトリ
    out_dir: 反転後の保存ディレクトリ
    """
    root_dir = '/usr/local/wk/git_local/bike/'
    target_dir = root_dir + 'analysis/front_fork/data/images/left/training_image/left_resize/'
    out_dir = root_dir + 'analysis/front_fork/data/cascade/left/images/reverse/'
    # 画像を反転して保存
    # reverse_save(target_dir, out_dir)

    # 座標を利用して、cascade検出器作成用のpositive.dat作成
    db_file = root_dir + 'analysis/front_fork/data/from_db/left/front_fork_left.tsv'
    reverse_positive_dat = root_dir + 'analysis/front_fork/data/cascade/right/datfile/positive_reverse_right.dat'
    make_positive(db_file, out_dir, reverse_positive_dat)


def make_positive(db_file, out_dir, reverse_positive_dat):
    reverse_image_list = os.listdir(out_dir)
    reverse_image_list = common_image.del_dsstore(reverse_image_list)
    print reverse_image_list
    with open(db_file, 'r') as dbf:
        for line in dbf:
            out_list = []
            line = line.rstrip()
            values = line.split('\t')
            image_name = values[2].split('/')[-1]
            if 'reverse_' + image_name not in reverse_image_list:
                continue
            processed = values[3]
            if processed != '1':
                continue
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
            ltx = 400.0 - ltx
            rtx = 400.0 - rtx
            lmx = 400.0 - lmx
            rmx = 400.0 - rmx
            lbx = 400.0 - lbx
            rbx = 400.0 - rbx

            x_min, x_max = min([ltx, rtx, lmx, rmx, lbx, rbx]), max([ltx, rtx, lmx, rmx, lbx, rbx])
            y_min, y_max = min([lty, rty, lmy, rmy, lby, rby]), max([lty, rty, lmy, rmy, lby, rby])

            x_min = x_min - 20.0 if x_min - 20.0 > 0 else x_min
            x_max = x_max + 20.0 if x_max + 20.0 < float(400) else x_max
            y_min = y_min - 20.0 if y_min - 20.0 > 0 else y_min
            y_max = y_max + 20.0 if y_max + 20.0 < float(300) else y_max

            out_list.append(out_dir + 'reverse_' + image_name)
            out_list.append('1')
            out_list.append(int(x_min))
            out_list.append(int(y_min))
            out_list.append(int(x_max - x_min))
            out_list.append(int(y_max - y_min))
            with open(reverse_positive_dat, 'a') as out_f:
                out_f.write(' '.join(map(str, out_list)) + '\n')


def reverse_save(target_dir, out_dir):
    image_name_list = os.listdir(target_dir)
    image_name_list = common_image.del_dsstore(image_name_list)
    for image_name in image_name_list:
        image = cv2.imread(target_dir + image_name, cv2.IMREAD_COLOR)
        if image is None:
            continue
        reverse_image = common_image.reverse_image(image, 1)
        save_name = out_dir + 'reverse_' + image_name
        common_image.save_image(reverse_image, save_name)


if __name__ == '__main__':
    main()
