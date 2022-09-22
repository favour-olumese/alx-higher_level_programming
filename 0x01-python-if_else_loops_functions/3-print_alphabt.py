#!/usr/bin/python3
num = 97
count = 0

while count < 26:
    alphabet = chr(num + count)

    if alphabet not in ['q', 'e']:
        print("{}".format(alphabet), end='')
    count += 1
