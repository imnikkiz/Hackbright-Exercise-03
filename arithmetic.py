def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    a = float(num1)
    b = float(num2)
    return a / b

def square(num1):
    return num1 * num1

def cube(num1):
    return num1 * num1 * num1

def power(num1, num2):
    return num1 ** num2

def mod(num1, num2):
    return num1 % num2

operators = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "square": square,
    "cube": cube,
    "pow": power,
    "mod": mod
}