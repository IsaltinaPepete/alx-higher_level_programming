#!/usr/bin/python3
""""Defines a method"""

def append_write(filename="", text=""):
    """define a method append
    Args:
        filename(string)- name of file
        text(string) - the text
    Returns:
        The number of characters appended.
    """
    with open(filename, "a+", encoding="utf-8") as f:
        f.seek(0, 2)
        return f.write(text)
