#!/usr/bin/python3
def no_c(my_string):
    my_string = "".join([c for c in my_string if c != "c" and c != "C"])
    return (my_string)
