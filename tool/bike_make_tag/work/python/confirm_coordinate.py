# -*- coding: utf-8 -*- 
import cv2
import matplotlib.pyplot as plt


def confirm_imshow(img):
    cv2.namedWindow('window')
    cv2.imshow('window', img)
    cv2.waitKey(0)

def save_img(img, img_name ,out_dir):
    cv2.imwrite(out_dir + img_name, img)

def confirm_coordinate(result_file, kbn):
    if kbn == 'db':
        with open(result_file, 'r') as in_f:
            for line in in_f:
                values = line.rstrip().split(' ')
                id = values[0]
                img_name = values[2].replace('images/left_resize', '')
                img_path = '../../data/resize_left/' + img_name
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
                confirm_imshow(img)
                out_dir = '../../data/resize_left_add_coordinate/'
                # save_img(img, img_name, out_dir)

    elif kbn == 'file':
        with open(result_file, 'r') as in_f:
            for line in in_f:
                values = line.rstrip().split(' ')
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

                # IDの追記
                cv2.putText(img,id,(520,40),cv2.FONT_HERSHEY_PLAIN, 2,(255, 255, 255))

                # 座標の追記
                cv2.circle(img, (point_ltx, point_lty), 3, (0, 255, 0), -1)
                cv2.circle(img, (point_rtx, point_rty), 3, (0, 255, 0), -1)
                cv2.circle(img, (point_lmx, point_lmy), 3, (0, 255, 0), -1)
                cv2.circle(img, (point_rmx, point_rmy), 3, (0, 255, 0), -1)
                cv2.circle(img, (point_lbx, point_lby), 3, (0, 255, 0), -1)
                cv2.circle(img, (point_rbx, point_rby), 3, (0, 255, 0), -1)
                confirm_imshow(img)
                out_dir = '../../data/resize_left_add_coordinate/'
                # save_img(img, img_name, out_dir)


if __name__ == '__main__':
    result_file = '../../data/bike_random_clop_coordinate_1.tsv'
    confirm_coordinate(result_file, 'file')
