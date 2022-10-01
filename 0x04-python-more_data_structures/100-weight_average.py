#!/usr/bin/python3
def weight_average(my_list=[]):
    weight_sum = 0
    freq = 0
    for x, y in my_list:
        weight_sum += x*y
        freq += y

    weight_ave = weight_sum/freq
    return weight_ave
