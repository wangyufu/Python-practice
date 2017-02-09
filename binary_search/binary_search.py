#!/usr/bin/env python

data = range(1, 1000000)


def binary_search(find_str, data_set):
    mid = int(len(data_set)/2)
    if mid == 0:
        if data_set[mid] == find_str:
            print("find it", find_str)
        else:
            print("cannot find this num in list", find_str)
        return

    if data_set[mid] == find_str:
        print('find it', find_str)
    elif data_set[mid] > find_str:
        print('going to search in left', data_set[mid], data_set[0:mid])
        binary_search(find_str, data_set[0:mid])
    else:
        print('going to search in right', data_set[mid], data_set[mid+1:])
        binary_search(find_str, data_set[mid+1:])

num = int(input('Input to find the number: '))
binary_search(num, data)