#!/usr/bin/python3
'''
Function for read a filetext
'''


def read_file(filename=""):
    '''
    Function for read a filetext
    '''
    with open(filename, 'r', encoding="UTF-8") as the_text:
        read_data = the_text.read()
    print(read_data, end="")
