#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        counter = 0
        if my_list[x]:
            for i in range(x):
                while True:
                    try:
                        print(int(my_list[i]), end="")
                        counter += 1
                    except (ValueError, TypeError):
                        pass
                    break
        print()
        return counter

    except IndexError:
        counter = 0
        for x in my_list:
            while True:
                try:
                    print(int(x), end="")
                    counter += 1
                except (ValueError, TypeError):
                    pass
                break
        print()
        return counter

# https://stackoverflow.com/a/2083996
