#!/usr/bin/python3
def roman_to_int(roman_string):
    numbers = {
        'M': 1000, 'CM': 1000, 'D': 500, 'CD': 400,
        'C': 100, 'XC': 90, 'L': 50, 'XL': 40,
        'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1
    }
    summation = 0
    i = 0

    if type(roman_string) != str or roman_string == None:
        return 0

    while i < len(roman_string):
        if roman_string[i:i+2] in numbers.keys():
            summation += numbers[roman_string[i:i+2]]
            i += 2
        elif roman_string[i] in numbers.keys():
            summation += numbers[roman_string[i]]
            i += 1
        else:
            return 0

    return summation
