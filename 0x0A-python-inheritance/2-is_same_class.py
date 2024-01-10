#!/usr/bin/python3
"""Define a class-checking function."""


def is_same_class(obj, a_class):

    if not isinstance(a_class, type):
        raise TypeError("a_class must be a type")
    return (type(obj) is a_class)
