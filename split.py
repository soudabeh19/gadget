#!/usr/bin/env python
import os,sys
import argparse
import pandas as pd
def parse_file(in_file):
    lines = []
    with open(in_file, 'r') as f:
        for line in f:
            elements = line.split(";")
            lines.append([int(elements[0]), int(elements[1]), int(elements[2]), int(elements[3])])
    #print("****************",max( lines, key=lambda x: x[0]))
    return lines


def write_line_list_to_text_file(line_list, file_name):
    with open(file_name, 'w') as f:
        for line in line_list:
            f.write("{0};{1};{2};{3}\n".format(line[0],line[1],line[2],line[3]))



def main(args=None):
    parser = argparse.ArgumentParser("split.py")
    parser.add_argument ("in_file", action="store", help = "input file in txt format")
    parser.add_argument ("max_x", action="store", help = "maximum x of matrix which is desired", type = int)
    parser.add_argument ("max_y", action="store", help = "maximum y of matrix which is desired", type = int)
    results = parser.parse_args() if args is None else parser.parse_args(args)
    lines = parse_file(results.in_file)
    dic = {}
    selected_in_range_lines = [] 
    file_index_list = []
    all_sub_inrange = []
    for line in lines:    
        if line[1] in range (0,results.max_x) and line[0] in range (0,results.max_y):
            selected_in_range_lines.append(line)
            #print (line)
    for i in range(len(selected_in_range_lines)):all_sub_inrange.append(selected_in_range_lines[i][1])
    sub_uniq = sorted(set(all_sub_inrange))
    for key in sub_uniq:
        dic[key]= []
        for t in selected_in_range_lines:
            if t[1] == key:
                dic[key].append(t[3])
    df = pd.DataFrame(dic)
    print (df)
    for key in range(len(dic)):
        sub_list_file = sorted (dic[key]) #sorted file of each subject 
        replace_list_file = dic[key]
        for f in sub_list_file:
            index_file= sub_list_file.index(f)
            for file_name in replace_list_file:
                if file_name == f:
                    replace_list_file[replace_list_file.index(file_name)]= index_file
    dff = pd.DataFrame(dic)
    print (dff)




   # for i in range(len(selected_in_range_lines)):file_index_list.append(selected_in_range_lines[i][3])
    #list_uniq = sorted(set(file_index_list))

    
    #print("** Before", selected_in_range_lines)
     #for j in value_list_key:
     #   a = j[3]
     #   j[3] =  list_uniq.index(a)

    #print("** After", selected_in_range_lines)
    #print("****************",max(selected_in_range_lines , key=lambda x: x[0]))
    write_line_list_to_text_file(selected_in_range_lines, "FS-First-bound-100files.txt")
	
 


if __name__ == "__main__":
    main()
