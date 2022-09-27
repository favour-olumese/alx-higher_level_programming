#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    summation = 0
    if len(argv) == 1:
        print("0")
    else:
        for args in argv[1:]:
            summation += int(args)
        print(summation)
