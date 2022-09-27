#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv) == 1:
        print("0 arguments.")
    else:
        if len(argv) == 2:
            print("1 argument:")
        else:
            print("{} arguments:".format(len(argv) - 1))

        for index, args in enumerate(argv[1:]):
            print("{}: {}".format(index + 1, args))
