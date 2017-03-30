#!/usr/bin/env sh

TOOLS=/usr/local/image_processing/caffe/build/tools

GLOG_logtostderr=1 $TOOLS/caffe train \
  --weights=./model/bvlc_reference_caffenet.caffemodel \
  --solver=./model/solver_quick.prototxt 2>&1  | tee ./model/log_quick.log
