"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""
from arithmetic import add, subtract, multiply, divide, square, cube, power, mod


def tokenize(comp):
    tokens = comp.strip()
    tokens = tokens.split()
    return tokens


def main():
    computing = True
    while computing == True:
        comp = tokenize(raw_input("> "))
        print comp
        if comp[0] == "q":
            computing = False


if __name__ == '__main__':
    main()
