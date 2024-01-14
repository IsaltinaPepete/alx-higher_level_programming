#!/usr/bin/python3

def uniq_add(my_list=[]):
    soma = 0
    unique_list = list(set(my_list))
    for i in unique_list:
        soma += i
    return soma
