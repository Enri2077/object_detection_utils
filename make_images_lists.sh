#!/bin/bash

# TODO get folder from param
# BASE_FOLDER=~/ds/yolo/etc
# cd $BASE_FOLDER

echo "Making list of train and test images in current folder "`pwd`

echo 'train/*.jpg > train.txt'
find `pwd`/train/ | sort | grep ".jpg" > train.txt &&

echo 'train_source/*.jpg >> train.txt' &&
find `pwd`/train_source/ | sort | grep ".jpg" >> train.txt

echo 'negative/*.jpg >> train.txt' &&
find `pwd`/negative/ | sort | grep ".jpg" >> train.txt

echo 'test_source/*.jpg > test.txt'
find `pwd`/test_source/ | sort | grep ".jpg" > test.txt

