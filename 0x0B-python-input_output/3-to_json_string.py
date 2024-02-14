#!/usr/bin/python3
"""define a method"""
import json


def to_json_string(my_obj):
    """Converte um objeto em sua representação JSON como uma string.

    Args:
    my_obj: the object .

    Retorna:
    str: A representação JSON do objeto como uma strin
    """
    json_string = json.dumps(my_obj)
    return json_string
