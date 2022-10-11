#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        if my_list[x]:
            for i in range(x):
                print(my_list[i], end="")
        print()
        return x
    except IndexError:
        i = 0
        for x in my_list:
            print(x, end="")
            i += 1
        print()
        return i
