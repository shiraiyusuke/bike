# -*- coding: utf-8 -*-
import numpy as np
import scipy as sc
import pandas as pd
import os
import sys


def make_jpglink(in_f, out_f):
    with open(in_data, 'r') as inf_list:
        out_str = ''
        for bike_id in inf_list:
            bike_id = bike_id.strip()
            out_str = out_str + 'http://picture.goobike.com/' + bike_id[0:3] + '/' + bike_id[0:7] + '/J/' + bike_id + '00.jpg' + '\n'
    with open(out_f, 'w') as out_f:
        out_f.write(out_str)

if __name__ == '__main__':
    target_brand_shashu = 'honda__cb1300_super_four' # yamaha__sr400
    in_data = '../data/' + target_brand_shashu + '_id_list.lst'
    out_data = '../data/' + target_brand_shashu + '_jpg_link.lst'
    make_jpglink(in_data, out_data)
