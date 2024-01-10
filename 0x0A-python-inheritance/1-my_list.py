#!/usr/bin/python3
""" has the Mylist class"""
class MyList(list):
    """subclass to add methods to list class"""
    def print_sorted(self):
        """prints sorted list"""
        print(sorted(self))
