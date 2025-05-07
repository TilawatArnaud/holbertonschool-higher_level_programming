#!/usr/bin/python3
import sys

if __name__ == "__main__":
    if len(sys.argv) == 0:
        print("0 arguments")
    elif len(sys.argv) == 1:
        print("1 argument:")
        print(f"1: argument {sys.argv}")
    else:
        print(f"{len(sys.argv[1:])} arguments:")
        for x in range (len(sys.argv[1:])):
            print(f"{x +1}: {sys.argv[x+1]}")
