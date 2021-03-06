#!/usr/bin/env python
"""
classify.py is an out-of-the-box image classifer callable from the command line.
By default it configures and runs the Caffe reference ImageNet model.
"""
import numpy as np
import pandas as pd
import os
import sys
import argparse
import glob
import time

import caffe
from PIL import Image


######## params ########
model_num = str(sys.argv[1])
K = int(sys.argv[2])
input_file = "./data/test_lst.txt"
image_dims = (256, 256)
crop_dims = (227, 227)
model_def = "./model/deploy.prototxt"
pretrained_model = "./model/net_iter_" + model_num + ".caffemodel"
mean_file = "./data/mean_train.npy"
center_only = False
gpu = True

batch_size = 100
#130000[ 0.78102837  0.97163121  0.9929078   0.9964539   1.        ]
#110000[ 0.78102837  0.97074468  0.99379433  0.99734043  1.        ]
#100000[ 0.78457447  0.97074468  0.99202128  0.9964539   1.        ]
#90000 [ 0.78280142  0.96985816  0.9929078   0.99734043  1.        ]
#70000 [ 0.77039007  0.96719858  0.9929078   0.9964539   1.        ]
#50000 [ 0.78368794  0.96542553  0.99468085  0.99734043  1.        ]
########################


# Make classifier.
tmp_x = int((image_dims[0] - crop_dims[0])/2.0)
tmp_y = int((image_dims[1] - crop_dims[1])/2.0)
crop_rect = (tmp_x, image_dims[0]-tmp_x, tmp_y, image_dims[1]-tmp_y)
print crop_rect
classifier = caffe.Classifier(model_def, pretrained_model,
                              image_dims=image_dims,gpu=gpu,
                              mean=np.load(mean_file)[:,crop_rect[0]:crop_rect[1],crop_rect[2]:crop_rect[3]])

#lst
lst_data = pd.read_csv(input_file, header = None, sep = " ")
lst_data.columns = ["path", "lab"]
pathes = lst_data["path"]
anses = lst_data["lab"]

l = len(pathes)
iter_num = int(np.ceil(l / float(batch_size)))
res = np.repeat(0,K)

for i in range(iter_num):
    print i*batch_size
    start_idx = i*batch_size
    end_idx = min((i+1)*batch_size, l)
    #load data
    inputs = [np.asarray(Image.open(im_f), dtype=np.float32) for im_f in pathes[start_idx:end_idx]]

    # Classify
    predictions = classifier.predict(inputs, not center_only)

    # top-K predict
    top_args = np.argsort(-predictions, axis=1)
    for top_arg,  ans in zip(top_args, anses[start_idx:end_idx]):
        for i in range(K):
            res[i] = res[i]+int(ans in top_arg[:(i+1)])


print res / float(len(pathes))






