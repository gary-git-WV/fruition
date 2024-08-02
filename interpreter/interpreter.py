def main():
    ''' Prompts user for arithmetic expression,
    then returns the result to one place float '''
    instring = input("Expression: ")
    inlist = instring.split()
    op1 = int(inlist[0])
    oper = inlist[1]
    op2 = int(inlist[2])
    if oper == '+':
        result = float(op1 + op2)
    elif oper == '-':
        result = float(op1 - op2)
    elif oper == '*':
        result = float(op1 * op2)
    elif oper == '/':
        result = float(op1 / op2)
    else:
        result = "invalid operator"
    print(result)

main()
