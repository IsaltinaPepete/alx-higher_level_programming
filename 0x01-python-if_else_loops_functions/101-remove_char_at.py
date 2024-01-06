#!/usr/bin/python3

def remove_char_at(str, n):
    teste = ""
    for i in range(0, len(str)):
        if i != n:
            teste+= str[i]
    return teste
