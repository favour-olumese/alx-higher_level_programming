#!/usr/bin/python3
def remove_char_at(str, n):
    new_str = ""
    for index, letter in enumerate(str):
        if index != n:
            new_str += letter
    return new_str
