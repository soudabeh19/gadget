#!/usr/bin/env python

import numpy as np
import csv
import argparse
import matplotlib
matplotlib.use('PS')
import matplotlib.pyplot as plt
def read_file(a,b,c,matrix,is_prediction):
    with open(matrix, 'rt') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            for row in reader:
                assert(len(row) >= 3)
                if is_prediction:
                    a.append(int(row[0]))#ordered_file_id
                    b.append(int(row[1]))#subject_id
                    c.append(float(row[3]))#predict-value
                else:
                    a.append(int(row[3]))#ordered_file
                    b.append(int(row[1]))#subject_id
                    c.append(int(row[2]))#differnce-value
    return(a,b,c)
def main():
    parser=argparse.ArgumentParser(description = "Plots a difference matrix.")
    
    
    parser.add_argument("--training","-t", help = "Matrix file to plot. Each row should be in the following format: <ignored> <subject_id> <binary_difference> <file_id>. File ids should be ordered according to their latest modification time.")# plotting training (row_index, subject, binary_difference, ordered_file_id)

    
    parser.add_argument("--prediction", "-p",help=" Matrix file to plot. Each row should be in the following format: <file_id> <subject_id> <ignored> <predic_value>. File ids should be ordered according to their latest modification time.")# plotting test (ordered_file_id, subject, binary_difference, predict_value)
    
    
    
    parser.add_argument("output_file", help = "Output file where the plot will be saved. File type is determined from extension.")
    args=parser.parse_args()
    a, b, c = ([] for i in range(3))
    if args.prediction:
        a,b,c = read_file(a,b,c,args.prediction, True)
        n = np.empty(shape=(max(a)+1,max(b)+1))
        n.fill(np.nan) #training elements won't get colored
    #for index, x in np.ndenumerate(n):
    #    print (index,x)
    if args.training:
        a,b,c = read_file(a,b,c,args.training, False)
        n = np.zeros(shape=(max(a)+1,max(b)+1))
    for i, x in enumerate(c):
        if args.training:
            n[a[i],b[i]] = 1 #c[i]
        else:
            n[a[i],b[i]] = c[i]
    plt.imshow(n, cmap='Reds', interpolation='none', aspect='auto')
    plt.xlabel('Subject')
    plt.ylabel('File-id')
    plt.colorbar()
    plt.savefig(args.output_file)

if __name__=='__main__':
    main()

