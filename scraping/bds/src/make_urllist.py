# -*- coding: utf-8 -*- 
import os
import sys


def function():
    pass


if __name__ == '__main__':
    in_file = '../data/output/CB1300_all.tsv'
    out_str = ''
    with open(in_file, 'r') as inf:
        for line in inf:
            line = line.strip()
            values = line.split('\t')
            for i in range(73, 79):
                out_str = out_str + values[i] + '\n'

    with open('url_list_CB1300.lst', 'w') as outf:
        outf.write(out_str)