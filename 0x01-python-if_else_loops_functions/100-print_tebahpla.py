#!/usr/bin/python3
for letter in range(122, 96, -1):
    if letter % 2 == 0:
        print("{}".format(chr(letter)), end="")
    else:
        aux = chr(ord(chr(letter)) - 32)
        print("{}".format(aux), end="")
