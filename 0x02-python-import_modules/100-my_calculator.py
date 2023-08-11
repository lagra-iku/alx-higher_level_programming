#!/usr/bin/python3
import sys
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    arg = sys.argv[1:]
    if len(arg) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    operators = {"+": add, "-": sub, "*": mul, "/": div}
    if arg[1] not in list(operators.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    a = int(arg[0])
    b = int(arg[2])
    print("{} {} {} = {}".format(a, arg[1], b, operators[arg[1]](a, b)))
