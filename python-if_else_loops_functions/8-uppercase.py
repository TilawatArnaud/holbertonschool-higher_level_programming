#!/usr/bin/python3
def uppercase(str):
    for x in str:
        if ord(str[x]) <= 97 and ord(str[x]) <= 122:
            print(chr(str[x] - 32))
        else:
            print(str[x])
