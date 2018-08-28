#!/usr/bin/env python

from __future__ import print_function
import os, sys
import pandas as pd
import matplotlib.pyplot as plt

def plot_file(file_paths, x, y):
    dfa  = pd.read_csv(file_paths[0], sep=', ', engine='python')
    dfa.columns = map(lambda s: (file_paths[0]+"/"+s) if s != x else s, dfa.columns.values)

    dfb  = pd.read_csv(file_paths[1], sep=', ', engine='python')
    dfb.columns = map(lambda s: (file_paths[1]+"/"+s) if s != x else s, dfb.columns.values)

    fig, axes = plt.subplots(nrows=1, ncols=len(y))
    
    for i in range(len(y)):
        y_a = file_paths[0]+"/"+y[i]
        y_b = file_paths[1]+"/"+y[i]
        ax = None
        ax = dfa.plot(x=x, y=y_a, ax=axes[i])    
        ax = dfb.plot(x=x, y=y_b, ax=axes[i])
        
        print("\nlast value of %s : %0.3f" % (file_paths[0]+"/\t"+y[i], list(dfa[y_a])[-1]))
        print(  "last value of %s : %0.3f" % (file_paths[1]+"/\t"+y[i], list(dfb[y_b])[-1]))
    
    plt.show()

def print_headers(file_path):
    dfa  = pd.read_csv(file_path, sep=', ', engine='python')
    print('header:')
    print("\n".join(map(lambda s: "'%s' " % s, list(dfa))))


if __name__ == "__main__":
    if len(sys.argv) in [2, 3]:
        print_headers(sys.argv[1])
    
    elif len(sys.argv) < 5:
        print("Args should be csv_a [csv_b x y+]")
        
    else:
        plot_file([sys.argv[1], sys.argv[2]], sys.argv[3], sys.argv[4:])
