#!/usr/bin/python3
"""method save"""
import json


def save_to_json_file(my_obj, filename):
    with open(filename, 'w') as file:
        json.load(my_obj, file)
