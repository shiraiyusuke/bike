# -*- coding: utf-8 -*-
import os

def make_list_fromdb():
    db_data = '/usr/local/wk/git_local/bike/analysis/front_fork/data/from_db/left_bike_coordinate_20170318.tsv'
    with open(db_data) as dbf:
        out_s = ''
        for line in dbf:
            values = line.split(' ')
            if values[0]=='image_id':
                continue
            image_path = values[2]
            image_name = image_path.split('/')[2]
            out_s = out_s + image_name + '\n'

    with open('./image_name.lst', 'w') as outf:
        outf.write(out_s)

def confirm_db_image():
    image_list = os.listdir('/usr/local/wk/git_local/bike/analysis/front_fork/data/images/training_image/resize_left/')
    print image_list
    tsv_list = []
    tsv_file = '/usr/local/wk/git_local/bike/analysis/front_fork/src/image_name.lst'
    with open(tsv_file, 'r') as inf:
        for line in inf:
            print line
            tsv_list.append(line.replace('\n', ''))
    print tsv_list
    matched_list = list(set(image_list) & set(tsv_list))
    print len(matched_list)

if __name__ == '__main__':
    confirm_db_image()
    # tsv_file = '/usr/local/wk/git_local/bike/analysis/front_fork/src/image_name.lst'
    # with open(tsv_file, 'r') as inf:
    #     for line in inf:
    #        print line