# -*- coding: utf-8 -*-
import os
import sys
import cv2
import random

def mk_450_600(img_list, org_dir, out_dir):
    for img in img_list:
        im = cv2.imread(org_dir + img)
        resize_img = cv2.resize(im, (600, 450))

        # cv2.imshow("resize", resize_img)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        cv2.imwrite(out_dir + img.replace('_300', '_450').replace('_400', '_600')  ,resize_img)

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


def resize_coordinate(coordinate_f, out_coordinate_f):
    with open(coordinate_f, 'r') as in_f:
        out_str = ''
        for line in in_f:
            values = line.rstrip().split(' ')
            out_list = []
            id = values[0]
            out_list.append(id)
            img_name = values[2].replace('images/left_resize', '')
            img_path = 'resize_left_450_600' + img_name.replace('_300', '_450').replace('_400', '_600')
            out_list.append(img_path)

            # img_path = '../../data/resize_left/' + img_name
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

            out_ltx = point_ltx * 1.5
            out_lty = point_lty * 1.5
            out_rtx = point_rtx * 1.5
            out_rty = point_rty * 1.5
            out_lmx = point_lmx * 1.5
            out_lmy = point_lmy * 1.5
            out_rmx = point_rmx * 1.5
            out_rmy = point_rmy * 1.5
            out_lbx = point_lbx * 1.5
            out_lby = point_lby * 1.5
            out_rbx = point_rbx * 1.5
            out_rby = point_rby * 1.5
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


def create_clop_coordinate(out_coordinate_f, out_random_clop_dir, aug_num):
    with open(out_coordinate_f, 'r')as in_f:
        out_str = ''
        for line in in_f:
            line = line.rstrip()
            values = line.split(' ')
            id = values[0]
            img_path = '../../data/' + values[1]
            point_ltx = int(values[2].split('.')[0])
            point_lty = int(values[3].split('.')[0])
            point_rtx = int(values[4].split('.')[0])
            point_rty = int(values[5].split('.')[0])
            point_lmx = int(values[6].split('.')[0])
            point_lmy = int(values[7].split('.')[0])
            point_rmx = int(values[8].split('.')[0])
            point_rmy = int(values[9].split('.')[0])
            point_lbx = int(values[10].split('.')[0])
            point_lby = int(values[11].split('.')[0])
            point_rbx = int(values[12].split('.')[0])
            point_rby = int(values[13].split('.')[0])

            img = cv2.imread(img_path)
            width = 400
            height = 300

            w_dist = random.randint(0,200)
            h_dist = random.randint(0,150)

            clop_img = img[h_dist:h_dist+height, w_dist:w_dist + width]
            # confirm_coordinate(clop_img)

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

            if point_lty < h_dist or (point_lty - h_dist > 300):
                point_lty = -1
            else:
                point_lty = point_lty - h_dist
            if point_rty < h_dist or (point_rty - h_dist > 300):
                point_rty = -1
            else:
                point_rty = point_rty - h_dist
            if point_lmy < h_dist or (point_lmy - h_dist > 300):
                point_lmy = -1
            else:
                point_lmy = point_lmy - h_dist
            if point_rmy < h_dist or (point_rmy - h_dist > 300):
                point_rmy = -1
            else:
                point_rmy = point_rmy - h_dist
            if (point_lby < h_dist) or (point_lby - h_dist > 300):
                point_lby = -1
            else:
                point_lby = point_lby - h_dist
            if point_rby < h_dist or (point_rby - h_dist > 300):
                point_rby = -1
            else:
                point_rby = point_rby - h_dist

            if point_ltx != -1 and point_lty != -1 and point_rtx != -1 and point_rty != -1 and point_lmx != -1 and point_lmy != -1 and \
                point_rmx != -1 and point_rmy != -1 and point_lbx != -1 and point_lby != -1 and point_rbx != -1 and point_rby != -1 :
                print point_ltx, point_lty, point_rtx, point_rty, point_lmx, point_lmy , point_rmx, point_rmy, point_lbx, point_lby, point_rbx, point_rby

                coordinate_tuple = (point_ltx, point_lty, point_rtx, point_rty, point_lmx, point_lmy, point_rmx, point_rmy, point_lbx, point_lby, point_rbx, point_rby)

                cv2.imwrite(out_random_clop_dir + str(aug_num) + '_' +values[1].split('/')[1].replace('_450','_300').replace('_600','_400'), clop_img)
                out_fname = out_random_clop_dir.replace('../../data/','') +  str(aug_num) +'_' +values[1].split('/')[1].replace('_450','_300').replace('_600','_400')
                out_str = out_str + id + '_aug'+ str(aug_num) + ' ' + out_fname + ' ' +' '.join(map(str, coordinate_tuple)) + '\n'

    with open('../../data/bike_random_clop_coordinate_' + str(aug_num) + '.tsv' , 'w') as out_f:
        out_f.write(out_str)

if __name__ == '__main__':
    org_dir = '../../data/resize_left/'
    img_list = os.listdir(org_dir)
    out_dir = '../../data/resize_left_450_600/'
    # 300 450から450 600を生成。
    # mk_450_600(img_list, org_dir, out_dir)
    coordinate_f = '../../data/bike_coordinate_20170120.tsv'
    out_coordinate_f = '../../data/bike_coordinate_20170120_450_600.tsv'
    # 450 600画像の座標を生成
    # resize_coordinate(coordinate_f, out_coordinate_f)

    # 450 600の画像を300 450でランダムにclopし、座標も修正
    out_random_clop_dir = '../../data/resize_random_clop_300_400/'
    create_clop_coordinate(out_coordinate_f, out_random_clop_dir, 4) # 第3引数はオーグメンテーションの回数
