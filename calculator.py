"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""
from arithmetic import add, subtract, multiply, divide, square, cube, power, mod


# def is_digits(comp):
#     '''takes list; breaks it down into characters; 
#     tests if each character after the operator is a digit'''
#     for operand in comp[1:]:
#         for char in operand:
#             if char not in ["0", "2", "3typ:
#                 print "Please make sure that you are entering only numbers after the operator."
#                 return False
#             else:
#                 return True


def calculate(comp):
    if len(comp) < 2:
        print "Please provide more information"
    elif len(comp) < 3:
        if comp[0] == "square":
            return square(comp[1])
        elif comp[0] == "cube":
            return cube(comp[1])
        else:
            print "Your chosen operator needs more numbers."
    elif comp[0] == "+":
        return add(comp[1], comp[2])
    elif comp[0] == "-":
        return subtract(comp[1], comp[2])
    elif comp[0] == "*":
        return multiply(comp[1], comp[2])
    elif comp[0] == "/":
        a = float(comp[1])
        b = float(comp[2])
        return divide(a, b)
    elif comp[0] == "pow":
        return power(comp[1], comp[2])
    elif comp[0] == "mod":
        return mod(comp[1], comp[2])
    else:
        print "I don't understand."


def tokenize(comp):
    '''takes in raw data and returns a list'''
    split = comp.split()
    operator = split[0]
    tokens = [operator]
    for past_one in split[1:]:
        try:
            tokens.append(int(float(past_one)))
        except ValueError:
            print "Please use numbers"
            return False
    return tokens


def main():
    '''takes raw_input (str); returns the answer'''
    computing = True
    while computing == True:
        comp = tokenize(raw_input("> "))
        if comp == False:
            print "Try again or type q"
        elif comp[0] == "q":
            computing = False
        else:
            answer = calculate(comp)
            print answer


if __name__ == '__main__':
    main() 