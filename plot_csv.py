#!/usr/bin/env python

from __future__ import print_function
import os, sys
import pandas as pd
import matplotlib.pyplot as plt

def plot_file(file_path, x, y = None):
    df  = pd.read_csv(file_path, sep=', ')
    
    print(list(df))
    
    if y == None:
        df.plot(x=x)
    else:
        df.plot(x=x, y=y)
    plt.show()

def print_headers(file_path):
    dfa  = pd.read_csv(file_path, sep=', ', engine='python')
    print('header:')
    print("\n".join(map(lambda s: "'%s' " % s, list(dfa))))

if __name__ == "__main__":
    if len(sys.argv) in [2, 3]:
        print_headers(sys.argv[1])
    
    elif len(sys.argv) < 4:
        print("Args should be (csv file) (x) [y]*")
        
    else:
        plot_file(sys.argv[1], sys.argv[2], sys.argv[3:])
