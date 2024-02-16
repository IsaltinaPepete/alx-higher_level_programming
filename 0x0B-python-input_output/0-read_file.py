#!/usr/bin/python3
"""Defines a read_file function"""


def read_file(filename=""):
    """read a file """
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read(), end="")
