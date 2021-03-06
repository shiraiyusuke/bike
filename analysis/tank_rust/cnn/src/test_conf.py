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
input_file = "./data/tes_0_500.txt"
image_dims = (256, 256)
crop_dims = (227, 227)
model_def = "./model/deploy.prototxt"
pretrained_model = "./model/net_iter_" + model_num + ".caffemodel"
mean_file = "./data/mean_train.npy"
center_only = False
gpu = True

batch_size = 100
########################


# Make classifier.
tmp_x = int((image_dims[0] - crop_dims[0])/2.0)
tmp_y = int((image_dims[1] - crop_dims[1])/2.0)
crop_rect = (tmp_x, image_dims[0]-tmp_x, tmp_y, image_dims[1]-tmp_y)
print crop_rect
classifier = caffe.Classifier(model_def, pretrained_model,
                              image_dims=image_dims,gpu=gpu,channel_swap=(2,1,0),
                              mean=np.load(mean_file)[:,crop_rect[0]:crop_rect[1],crop_rect[2]:crop_rect[3]])

#lst
lst_data = pd.read_csv(input_file, header = None, sep = " ")
lst_data.columns = ["path", "lab"]
pathes = lst_data["path"]
anses = lst_data["lab"]

l = len(pathes)
iter_num = int(np.ceil(l / float(batch_size)))
pred_label = []

for i in range(iter_num):
    print i*batch_size
    start_idx = i*batch_size
    end_idx = min((i+1)*batch_size, l)
    #load data
    inputs = [np.asarray(Image.open(im_f), dtype=np.float32) for im_f in pathes[start_idx:end_idx]]

    # Classify
    predictions = classifier.predict(inputs, not center_only)

    top_arg = predictions.argmax(axis=1)
    pred_label.extend(top_arg)


conf_data = pd.DataFrame({"pred":pred_label, "ans":anses})
print (conf_data.ans == conf_data.pred).sum()/float(l)
print pd.crosstab(conf_data["ans"], conf_data["pred"])
