#!/usr/bin/env python

from __future__ import print_function
import os, sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def plot_file(file_path, y = None):
    df  = pd.read_csv(file_path, sep=', ', engine='python')
    
    if y == None:
        y = list(df)
    
    print("using columns:", y)
    
    print("\nlast")
    print(', '.join(y))
    print(', '.join(map(lambda i: "%0.4f" % list(df[i])[-1], y)))
    
    print("\nmax")
    print(', '.join(y))
    print(', '.join(map(lambda i: "%0.4f" % np.max(list(df[i])[-11:-1]), y)))
    
    print("\nmin")
    print(', '.join(y))
    print(', '.join(map(lambda i: "%0.4f" % np.min(list(df[i])[-11:-1]), y)))
    
    print("\navg")
    print(', '.join(y))
    print(', '.join(map(lambda i: "%0.4f" % np.average(list(df[i])[-11:-1]), y)))

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Args should be csv_file y*")
    elif len(sys.argv) == 2:
        plot_file(sys.argv[1])
    elif len(sys.argv) > 2:
        plot_file(sys.argv[1], sys.argv[2:])
