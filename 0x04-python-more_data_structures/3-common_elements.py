#!/usr/bin/python3
def common_elements(set_1, set_2):
    # intersection = {x for x in set_1 if x in set_2}
    intersection = set_1 & set_2
    return intersection
