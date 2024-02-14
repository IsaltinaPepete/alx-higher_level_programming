#!/usr/bin/python3
"""define a method"""


def to_json_string(my_obj):
    """Converte um objeto em sua representação JSON como uma string.

    Args:
    my_obj: the object .

    Return:
    str: s string.
    """
    json_string = json.dumps(my_obj)
    return json_string
