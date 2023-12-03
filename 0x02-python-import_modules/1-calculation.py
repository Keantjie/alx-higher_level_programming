#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

def main():
    a = 10
    b = 5
    symbol = ['+', '-', '*', '/']
    op = {0: add, 1: sub, 2: mul, 3: div}
    for j in op:
        print('{:d} {:} {:d} = {:d}'.format(a, symbol[j], b, op[j](a, b)))

        if __name__ == "__main__":
            main()
