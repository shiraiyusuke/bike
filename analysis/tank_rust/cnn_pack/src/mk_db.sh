#!/usr/bin/env sh



#caffe/build/toolsへのパス
CAFFE_TOOLS=/usr/local/image_processing/caffe_20150401/build/tools
TOOLS=/usr/local/image_processing/work/tools


#ワーキングディレクトリ
WORK_DIR=./data

#学習に用いる画像のリスト
#<画像パス　ラベル>の形式
#ラベルは0から始まる通し番号に限る
TRAIN_PATH=$WORK_DIR/train.txt

#検証に用いる画像のリスト
#<画像パス　ラベル>の形式
#ラベルは0から始まる通し番号に限る
TEST_PATH=$WORK_DIR/test.txt

#出力DB名
TRAIN_DB=train_lmdb
TEST_DB=test_lmdb


#画像の平均値ファイルの出力先
#バイナリ形式
MEAN_PROTO_PATH=$WORK_DIR/mean_train.proto
#numpy配列形式
MEAN_NPY_PATH=$WORK_DIR/mean_train.npy

#グレイスケールにするか
GRAY_F=0

#リサイズ後の画像サイズ
HEIGHT=256
WIDTH=256

convert_train_all() {
    rm -rf $WORK_DIR/$TRAIN_DB
    if [ $GRAY_F = 0 ] ; then
        echo "======= not gray ======="
        $CAFFE_TOOLS/convert_imageset.bin -resize_height $HEIGHT -resize_width $WIDTH \
            -shuffle / $TRAIN_PATH $WORK_DIR/$TRAIN_DB
    else
        echo "======= gray ======="
        $CAFFE_TOOLS/convert_imageset.bin -resize_height $HEIGHT -resize_width $WIDTH \
            -gray -shuffle / $TRAIN_PATH $WORK_DIR/$TRAIN_DB
    fi
    echo "======= compute mean ======="
    $CAFFE_TOOLS/compute_image_mean.bin $WORK_DIR/$TRAIN_DB $MEAN_PROTO_PATH #lmdb
    echo "======= mean2npy ======="
    python $TOOLS/mean2npy.py $MEAN_PROTO_PATH $MEAN_NPY_PATH
}

convert_test() {
    rm -rf $WORK_DIR/$TEST_DB
    if [ $GRAY_F = 0 ] ; then
        echo "======= not gray ======="
        $CAFFE_TOOLS/convert_imageset.bin -resize_height $HEIGHT -resize_width $WIDTH \
            -shuffle / $TEST_PATH $WORK_DIR/$TEST_DB
    else
        echo "======= gray ======="
        $CAFFE_TOOLS/convert_imageset.bin -resize_height $HEIGHT -resize_width $WIDTH \
            -gray -shuffle / $TEST_PATH $WORK_DIR/$TEST_DB
    fi
}






case "$1" in
    "convert_train_all" )
        convert_train_all ;;
    "convert_test" )
        convert_test ;;
    "all" )
	echo ${TRAIN_PATH}
        convert_train_all
        convert_test
#        break ;;
esac




