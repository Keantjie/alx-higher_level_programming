#!usr/bin/python3
def multiply_by_2(a_dictionary):
    the_dict = {}
    for key, value in a_dictionary.items():
        the_dict.update({key: (value * 2)})
    return the_dict
