#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_list = list(set(my_list))
    summation = 0
    for num in unique_list:
        summation += num

    return summation
