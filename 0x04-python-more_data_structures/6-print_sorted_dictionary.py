#!/usr/bin/python3
def print_sorted_dictionary(my_dict):
    for the_key in sorted([key for key in my_dict]):
        print("{}: {}".format(the_key, my_dict[the_key]))
