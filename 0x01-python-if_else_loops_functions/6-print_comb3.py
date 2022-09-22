#!/usr/bin/python3
num = []
for i in range(1, 100):
    # The last number is not to have a comma
    if i == 89:
        print("{}".format(i))
        num.append(str(i))
        i += 1

    # Add 0 before numbers less than 10
    if i < 10:
        print("{:>02d}".format(i), end=", ")
    if i % 10 == 0:
        i += 1

    # Check the reverse of each number if they have a mirror number in the list
    # If they don't print and add them to the list.
    if i > 10 and str(i)[::-1] not in num:
        if str(i)[0] != str(i)[-1]:
            print("{}".format(i), end=", ")
            num.append(str(i))
