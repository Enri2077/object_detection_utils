#!/usr/bin/env python

from __future__ import print_function
import os, sys, re
from parse import *


p="{}\
BEGIN TEST {}yolov3-erl4_{}.weights{}detections_count = {}, unique_truth_count = {}  \n\
 rank ={}\
class_id = 0, name = mug_black, 	 ap = {} % \n\
class_id = 1, name = mug_gray, 	 ap = {} % \n\
class_id = 2, name = cocacola, 	 ap = {} % \n\
class_id = 3, name = pringles, 	 ap = {} % \n\
 for thresh = {}, precision = {}, recall = {}, F1-score = {} \n\
 for thresh = {}, TP = {}, FP = {}, FN = {}, average IoU = {} % \n\
\n\
 mean average precision (mAP) = {}, or {} %\
{}\
"


def parse_file(file_path):
    
    print("Parsing file", file_path, "...")
    
    with open(file_path[:-4]+".csv", 'w') as f_csv:
        
        d_list = []
        
        with open(file_path, 'r') as f:
        
            for s in f.read().split("END TEST"):
                prs = parse(p, s)
                if prs == None:
                    print("UNMATCHED:")
                    print("------------------------------")
                    print(s)
                    print("------------------------------")
                    # d_list += [{'w': None, 'detections_count': None, 'unique_truth_count': None, 'mug_black': None, 'mug_gray': None, 'cocacola': None, 'pringles': None, 'thresh': None, 'precision': None, 'recall': None, 'F1-score': None, 'TP': None, 'FP': None, 'FN': None, 'average IoU': None, 'mAP': None}]
                    continue
                    
                l = list(parse(p, s))[1:]
                
                try:
                    
                    # TODO workaround to count final as weight index!!
                    
                    if l[1] == 'final':
                        l[1] = '51000'
                    
                    d = {'w':int(l[1]), 'detections_count': int(l[3]), 'unique_truth_count': int(l[4]), 'mug_black': float(l[6])/100.0, 'mug_gray': float(l[7])/100.0, 'cocacola': float(l[8])/100.0, 'pringles': float(l[9])/100.0, 'thresh': float(l[10]), 'precision': float(l[11]), 'recall': float(l[12]), 'F1-score': float(l[13]), 'TP': int(l[15]), 'FP': int(l[16]), 'FN': int(l[17]), 'average IoU': float(l[18])/100.0, 'mAP': float(l[19])}
                    d_list += [d]
                 
                except ValueError:
                    tmp = {'w':l[1], 'detections_count': l[3], 'unique_truth_count': l[4], 'mug_black': l[6], 'mug_gray': l[7], 'cocacola': l[8], 'pringles': l[9], 'thresh': l[10], 'precision': l[11], 'recall': l[12], 'F1-score': l[13], 'TP': l[15], 'FP': l[16], 'FN': l[17], 'average IoU': l[18], 'mAP': l[19]}
                    print("Some values could not be converted:", tmp)
                    continue
                 
                 
#                for k in d.keys():
#                    print(k, '\t', d[k])
        
        f_csv.write("w, detections_count, unique_truth_count, mug_black average precision, mug_gray average precision, cocacola average precision, pringles average precision, precision, recall, F1-score, TP, FP, FN, average IoU, mAP\n")
        
        d_list.sort(key=lambda x: int(x['w']))        
        for d in d_list:
            f_csv.write(', '.join(map(str, [d['w'], d['detections_count'], d['unique_truth_count'], d['mug_black'], d['mug_gray'], d['cocacola'], d['pringles'], d['precision'], d['recall'], d['F1-score'], d['TP'], d['FP'], d['FN'], d['average IoU'], d['mAP']])) + '\n')
    
    print("Done.")

if __name__ == "__main__":
    print(sys.argv)
    if len(sys.argv) < 2:
        print("first arg should be file to parse")
        sys.exit(0)
    else:
        for a in sys.argv[1:]:
            parse_file(a)
