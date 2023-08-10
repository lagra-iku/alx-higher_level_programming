#!/usr/bin/python3
import sys
if __name__ == "__main__":
    arg_len = len(sys.argv)
    i = 0
    if arg_len >= 2:
        if arg_len == 2:
            print("{} argument:".format(arg_len - 1))
        else:
            print("{} arguments:".format(arg_len - 1))
        for x in sys.argv:
            if i == 0:
                i = i + 1
                continue
            print(f"{i}: {x}")
            i = i + 1
    else:
        print("0 arguments:")
