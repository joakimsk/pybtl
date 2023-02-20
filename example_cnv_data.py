#!/usr/bin/env python

import pyseabird

def other():
    valid_keys = pyseabird.GenericHashHeaderCnv
    for item in valid_keys:
        print(item)
    enumerate_list = [(index, element) for index, element in enumerate(valid_keys)]
    for idx, elem in enumerate_list:
        print(idx, elem.value)

def main():
    cnvfile = pyseabird.Cnv("sta0078.cnv")
    
    for column in cnvfile.column_header_list.column_headers:
        print(column)
    #print(cnvfile.hash_header)
    #print(cnvfile.hash_name_dict)
    #print(cnvfile.hash_span_dict)
    #print(cnvfile.sensor_list)

if __name__ == '__main__':
    main()