import os
import cv2
import sys
import os
import common_image as ci


def make_clop_image(target_dir, out_coordinate_file, out_clop_image_dir, out_clop_gray_image_dir):
    with open(out_coordinate_file, 'r') as coordf:
        for line in coordf:
            values = line.rstrip().split('\t')
            image_name = values[0]
            xmin = float(values[1])
            xmax = float(values[2])
            ymin = float(values[3])
            ymax = float(values[4])
            range = (ymin, ymax, xmin, xmax)
            image = cv2.imread(target_dir + image_name)
            clop_image = ci.clop_image(image, range)
            save_name = out_clop_image_dir + 'forkclop_' + image_name
            ci.save_image(clop_image, save_name)

            gray_image = ci.gray_convert(clop_image)
            save_gray_name = out_clop_gray_image_dir + 'gray_' + image_name
            ci.save_image(gray_image, save_gray_name)


def make_square_file(in_db_file, out_square_file, input_size):
    if os.path.exists(out_square_file):
        os.remove(out_square_file)

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
            with open(out_square_file, 'a') as outf:
                outf.write('\t'.join(map(str, out_list)) + '\n')

if __name__ == '__main__':
    root_dir = '/usr/local/wk/git_local/bike/'
    in_db_file = root_dir + 'analysis/front_fork/data/from_db/bike_result_20170412_right.tsv'
    target_dit = root_dir + 'analysis/front_fork/data/images/training_image/right_resize/'
    out_square_file = root_dir + 'analysis/front_fork/data/fork_clop/square/square_right.tsv'
    out_clop_image_dir = root_dir + 'analysis/front_fork/data/images/fork_clop/right/training_image/color/'
    if not os.path.exists(out_clop_image_dir):
        os.mkdir(out_clop_image_dir)
    out_clop_gray_image_dir = root_dir + 'analysis/front_fork/data/images/fork_clop/right/training_image/gray/'
    if not os.path.exists(out_clop_gray_image_dir):
        os.mkdir(out_clop_gray_image_dir)
    input_size = (400, 300)
    # make_square_file(in_db_file, out_square_file, input_size)
    make_clop_image(target_dit, out_square_file, out_clop_image_dir, out_clop_gray_image_dir)

