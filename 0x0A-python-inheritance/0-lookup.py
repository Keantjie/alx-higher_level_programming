#!/usr/bin/python3
"""
Defines an object attribute lookup function.
"""


def lookup(obj):
    """
Return a list of the object that is available.
"""
    return (dir(obj))
