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
        a = float(comp[1])
        b = float(comp[2])
        return divide(a, b)
    elif comp[0] == "square":
        return square(comp[1])
    elif comp[0] == "cube":
        return cube(comp[1])
    elif comp[0] == "pow":
        return power(comp[1], comp[2])
    elif comp[0] == "mod":
        return mod(comp[1], comp[2])
    else:
        print "I don't understand."


def tokenize(comp):
    split = comp.split()
    operator = split[0]
    tokens = [operator]
    for i in range(len(split)-1):
        tokens.append(int(split[i+1]))
    return tokens


def main():
    computing = True
    while computing == True:
        comp = tokenize(raw_input("> "))
        if comp[0] == "q":
            computing = False
        else:
            answer = calculate(comp)
            print answer


if __name__ == '__main__':
    main()

#  To Do:
#  + 1
#  + 1 a
