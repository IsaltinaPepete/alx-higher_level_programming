#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1) 
    if sys.argv[2] == '+':
        print("{} + {} = {}".format(sys.argv[1], sys.argv[3], add(sys.argv[1], sys.argv[3])))
        sys.exit(0)
    elif sys.argv[2] == '-':
        print("{} - {} = {}".format(sys.argv[1], sys.argv[3], sub(sys.argv[1], sys.argv[3])))
        sys.exit(0)
    elif sys.argv[2] == '*':
        print("{} * {} = {}".format(sys.argv[1], sys.argv[3], mul(sys.argv[1], sys.argv[3])))
        sys.exit(0)
    elif sys.argv[2] == '/':
        print("{} / {} = {}".format(sys.argv[1], sys.argv[3], div(sys.argv[1], sys.argv[3])))
        sys.exit(0)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(0)
