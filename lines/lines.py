import sys
'''a program that expects exactly one command-line argument, the name
(or path) of a Python file, and outputs the number of lines of code in that
file, excluding comments and blank lines'''

def main():
    inFileName = getInput()
    if inFileName == 0:
        sys.exit
    print(inFileName)



def getInput():
    # read cli into "input"
    input = sys.argv
    # input must include only one argument (a filename)
    if len(input) < 2:
        sys.exit("Too few command-line arguments ")
    elif len(input) > 2:
         sys.exit("Too many command-line arguments ")
    # file must exist
    try:
        file = open(input[1], "r")
    except FileNotFoundError:
        sys.exit("File does not exist")
    file.close()
    # file must be  a python file
    if input[1].endswith != 'py':
        sys.exit("Not a Python file ")



    inFileName = input[1]
    return(inFileName)




if __name__ == "__main__":
    main()
