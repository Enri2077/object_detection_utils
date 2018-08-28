#!/usr/bin/env python

from __future__ import print_function
import os, sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def plot_file(file_path, y = None, x = None):
    df  = pd.read_csv(file_path, sep=', ', engine='python')
    
    if y == None:
        y = list(df)
    
    if x == None:
        format_string = "%0.4f"
    else:
        format_string = "%0.4f @ %s"
    
    print("using columns:", y)
    print("using x:", x)
    
    
    
    print("\nlast")
    print(', '.join(y))
    if x: print(', '.join(map(lambda i: "%0.4f @ %s" % (list(df[i])[-1], list(df[x])[-1]), y)))
    else: print(', '.join(map(lambda i: "%0.4f" % list(df[i])[-1], y)))
    
    print("\nmax of last 10")
    print(', '.join(y))
    if x: print(', '.join(map(lambda i: "%0.4f @ %s" % (np.nanmax(list(df[i])[-11:-1]), list(df[x])[np.nanargmax(list(df[i])[-11:-1])]), y)))
    else: print(', '.join(map(lambda i: "%0.4f" % np.nanmax(list(df[i])[-11:-1]), y)))
    
    print("\nmin of last 10")
    print(', '.join(y))
    if x: print(', '.join(map(lambda i: "%0.4f @ %s" % (np.nanmin(list(df[i])[-11:-1]), list(df[x])[np.nanargmin(list(df[i])[-11:-1])]), y)))
    else: print(', '.join(map(lambda i: "%0.4f" % np.nanmin(list(df[i])[-11:-1]), y)))
    
    print("\navg of last 10")
    print(', '.join(y))
    print(', '.join(map(lambda i: "%0.4f" % np.nanmean(list(df[i])[-11:-1]), y)))

    print("\nmax")
    print(', '.join(y))
    if x: print(', '.join(map(lambda i: "%0.4f @ %s" % (np.nanmax(list(df[i])), list(df[x])[np.nanargmax(list(df[i]))]), y)))
    else: print(', '.join(map(lambda i: "%0.4f" % np.nanmax(list(df[i])), y)))
    
    print("\nmin")
    print(', '.join(y))
    if x: print(', '.join(map(lambda i: "%0.4f @ %s" % (np.nanmin(list(df[i])), list(df[x])[np.nanargmin(list(df[i]))]), y)))
    else: print(', '.join(map(lambda i: "%0.4f" % np.nanmin(list(df[i])), y)))
    
    print("\navg")
    print(', '.join(y))
    print(', '.join(map(lambda i: "%0.4f" % np.nanmean(list(df[i])), y)))

def print_headers(file_path):
    dfa  = pd.read_csv(file_path, sep=', ', engine='python')
    print('header:')
    print("\n".join(map(lambda s: "'%s' " % s, list(dfa))))

if __name__ == "__main__":
    l = len(sys.argv)
    if l == 1:
        print("Args should be csv_file [[-x x] y+]")
    elif l == 2:
        print_headers(sys.argv[1])
    elif l > 2:
        if sys.argv[2] == '-x':
            if l < 4:
                print("Args should be csv_file [-x x] y*")
            else:
                plot_file(sys.argv[1], sys.argv[4:], sys.argv[3])
        else:
            plot_file(sys.argv[1], sys.argv[2:])
