#!/usr/bin/python3
"""module evaluate geometry using maths operations"""


class BaseGeometry(object):
    """Geometry class with maths operations"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if (value.__class__ != int):
            raise TypeError("{:} must be an integer".format(name))
        if (value <= 0):
            raise ValueError("{:} must be greater than 0".format(name))
