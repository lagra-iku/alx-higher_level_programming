#!/usr/bin/python3
import sys
if __name__ == "__main__":
    args = sys.argv[1:]
    i = 1
    if len(args) == 0:
        print("0 arguments.")
    elif len(args) == 1:
        print("{} argument:".format(len(args)))
    else:
        print("{} arguments:".format(len(args)))
    for arg in args:
        print("{}: {}".format(i, arg))
        i = i + 1
