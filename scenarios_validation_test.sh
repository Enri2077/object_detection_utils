#!/usr/bin/env bash

NOW=`date -Iseconds`
DARKNET=~/w/yolo_ws/gpu_darknet/darknet
CFG_FILE=~/w/yolo_ws/gpu_darknet/cfg/yolov3-erl4-testing.cfg

SCENARIO_LIST="\
coffee_table
kitchen
real_kitchen
shelf
table_high
window
grasped_cocacola
grasped_move
grasped_mug_black
grasped_mug_gray
grasped_pringles
hand"

THRESH_LIST="\
0.5
0.9"

W_LIST="\
$HOME/w/yolo_ws/weights/erl4_v0_1/yolov3-erl4_final.weights
$HOME/w/yolo_ws/weights/erl4_v2/yolov3-erl4_21280.weights
$HOME/w/yolo_ws/weights/erl4_v3_1/yolov3-erl4_final.weights
$HOME/w/yolo_ws/weights/erl4_v4/yolov3-erl4_final.weights
$HOME/w/yolo_ws/weights/erl4_v5/yolov3-erl4_final.weights
$HOME/w/yolo_ws/weights/erl4_v6/yolov3-erl4_final.weights
$HOME/w/yolo_ws/weights/erl4_v7/yolov3-erl4_45656.weights"


for w_file in $W_LIST; do
    for thresh in $THRESH_LIST; do
	    for scenario in $SCENARIO_LIST; do
	        data_file="$HOME/w/yolo_ws/gpu_darknet/cfg/erl4_$scenario.data"
	        
	        OUTPUT_FILE=test_results_t$thresh-$scenario.txt #-$NOW.txt
	        
	        echo "$DARKNET detector map $data_file $CFG_FILE $w_file -thresh $thresh >> $OUTPUT_FILE"
	        
            echo "
            
            BEGIN TEST $w_file
            " >> $OUTPUT_FILE
            
            $DARKNET detector map $data_file $CFG_FILE $w_file -thresh $thresh >> $OUTPUT_FILE
            echo "
            END TEST
            " >> $OUTPUT_FILE
            
        done
    done
done
