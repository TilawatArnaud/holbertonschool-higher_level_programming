#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return (0)
    if idx > len(my_list):
        return (None)
    else:
        print("{}".format(my_list[idx]))
