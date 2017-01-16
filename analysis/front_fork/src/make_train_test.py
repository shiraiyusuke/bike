# -*- coding: utf-8 -*-
import os
import sys
import numpy as np
import pandas as pd
import analysis.front_fork.entity.dbresult as ent_bike

def make_train_test_csv(result_file, o_training_file, o_test_file):
    entity_cls = getattr(sys.modules['analysis.front_fork.entity.dbresult'].DBresult, 'dbresult')
    print(entity_cls)

if __name__ == '__main__':
    result_file = '../data/bike_result_all.tsv'
    o_training_file = '../data/training.csv'
    o_test_file = '../data/test.csv'
    make_train_test_csv(result_file, o_training_file, o_test_file)