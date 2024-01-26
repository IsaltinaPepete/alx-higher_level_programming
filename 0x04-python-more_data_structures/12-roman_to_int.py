#!/usr/bin/python3

def roman_to_int(roman_string):
    roman  = {"X": 10, "I": 1, "V": 5, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = 0
    i = 0

    while i < len(roman_string):
        if i+1 < len(roman_string) and roman[roman_string[i]] < roman[roman_string[i+1]]:
            result += roman[roman_string[i+1]] - roman[roman_string[i]]
            i += 2
        else:
            result += roman[roman_string[i]]
            i += 1

    return result
