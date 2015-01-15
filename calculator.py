"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""
from arithmetic import add, subtract, multiply, divide, square, cube, power, mod
def calculate(comp):
    if comp[0] == "+":
        return add(comp[1], comp[2])
    elif comp[0] == "-":
        return subtract(comp[1], comp[2])
    elif comp[0] == "*":
        return multiply(comp[1], comp[2])
    elif comp[0] == "/":
        return divide(comp[1], comp[2])



def tokenize(comp):
    tokens = comp.strip()
    tokens = tokens.split()
    operator = tokens[0]
    a = int(tokens[1])
    b = int(tokens[2])
    tokens = [operator, a, b]
    return tokens



def main():
    computing = True
    while computing == True:
        comp = tokenize(raw_input("> "))
        print comp
        if comp[0] == "q":
            computing = False
        else:
            answer = calculate(comp)
            print answer


if __name__ == '__main__':
    main()
