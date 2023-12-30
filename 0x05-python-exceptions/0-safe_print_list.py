#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    kea = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            kea += 1
        except IndexError:
            break
    print("")
    return (kea)
