from arithmetic import operators


def instructions():
    print """
    Instructions: 

    Choose one operator from the list 
        and provide the required number of operands:

    Operator        
           Operands 
                 Function

    +      1 2   add numbers 1 and 2
    -      1 2   subtract number 2 from number 1
    *      1 2   multiply numbers 1 and 2
    /      1 2   divide number 1 by number 2
    square 1     square the number
    cube   1     cube the number
    pow    1 2   raise number 1 to the power of number 2
    mod    1 2   return the remainder of number 1 divided by number 2

    q            quit

    """


def calculate(oper_list):
    """ Computes digits by given operator. 

    Returns None if successful, False if incorrect number of operands.
    """
    if len(oper_list) == 2:
        try:
            print operators[oper_list[0]](oper_list[1])
        except TypeError:
            print "Error! Please provide two operands."
            return False
    else:
        try:
            print operators[oper_list[0]](oper_list[1], oper_list[2])
        except TypeError:
            print "Error! Please provide no more than one operand."
            return False


def tokenize(input_string):
    """ Converts raw data to list of [operator, digit(s)]. 

    Returns list, "quit", or False (if incorrect length or not digits). 
    """         
    if input_string == "q":
        return "quit"

    split = input_string.split()
        
    if (len(split) < 2 or
       len(split) > 3 or 
       split[0] not in operators):
        print "Error! Please provide an operator and one or two operands."
        return False

    tokens = [split[0]]

    for past_one in split[1:]:
        try:
            tokens.append(int(float(past_one)))
        except ValueError:
            print "Error! Please use numbers."
            return False
    return tokens


def main():
    """ Initiate calculator and compute input.

    Program will call instructions, then tokenize, then calculate. 
    """
    instructions()
    while True:
        # Both tokenize and calculate can return False if user input
        # is incalculable. The assigned tokenized_input will then be False.
        tokenized_input = tokenize(raw_input("> "))
        if tokenized_input == "quit":
            break 
        if tokenized_input:
            tokenized_input = calculate(tokenized_input)   
        if tokenized_input == False:  
            instructions()


if __name__ == '__main__':
    main() 