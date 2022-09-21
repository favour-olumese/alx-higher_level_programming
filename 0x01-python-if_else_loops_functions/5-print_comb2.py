#!/usr/bin/python3
for i in range(100):
    if i == 99:
        print(i)
    elif i < 10:
        print(f"{i:>02d}", end=", ")
    else:
        print(f"{i}", end=", ")
