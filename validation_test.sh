#!/usr/bin/env bash

NOW=`date -Iseconds`
DARKNET=~/w/yolo_ws/gpu_darknet/darknet
#DATA_FILE=~/w/yolo_ws/gpu_darknet/cfg/erl4.data
CFG_FILE=~/w/yolo_ws/gpu_darknet/cfg/yolov3-erl4-testing.cfg
#W_FOLDER=~/w/yolo_ws/weights/erl4_v2_1
#THRESH=0.25

echo "



PARAMS:
DATA_FILE: $DATA_FILE
CFG_FILE: $CFG_FILE
W_FOLDER: $W_FOLDER
THRESH: $THRESH

" >> test_results_$NOW.txt

for w_file in `ls $W_FOLDER/*.weights -t`; do
	echo "$DARKNET detector map $DATA_FILE $CFG_FILE $w_file >> test_results_$NOW.txt"
	
	echo "
	
	BEGIN TEST $w_file
	" >> test_results_$NOW.txt
	
	$DARKNET detector map $DATA_FILE $CFG_FILE $w_file -thresh $THRESH >> test_results_$NOW.txt
	
	echo "
	END TEST
	" >> test_results_$NOW.txt
	
done
