#!/usr/bin/env sh

TOOLS=/usr/local/image_processing/caffe/build/tools

GLOG_logtostderr=1 $TOOLS/caffe train \
  --weights=./model/bvlc_reference_caffenet.caffemodel \
  --solver=./model/solver.prototxt 2>&1  | tee ./model/log.log
