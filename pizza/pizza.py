'''expects exactly one command-line argument, the name (or path) of a CSV
file in Pinocchio/’s format, and outputs a table formatted as ASCII art'''
import sys
import csv
from tabulate import tabulate

def main():
    inFileName = getInput()
    if inFileName == 0:
        sys.exit
    makeTable(inFileName)
    return 0

def makeTable(inFileName):
    # init a list to hold data
    menu = []
    # open file, read data
    with open(inFileName, newline='') as csvfile:
        menureader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in menureader:
            menu.append(row)
    # use tabulate lib to print grid menu
    print(tabulate(menu[1:], menu[0], tablefmt="grid"))
    return 0

def getInput():
    # input must include only one argument (a filename)
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments ")
    elif len(sys.argv) > 2:
         sys.exit("Too many command-line arguments ")
    # file must exist
    try:
        file = open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("File does not exist")
    file.close()
    # file must be  a CSV file
    if not sys.argv[1].endswith('csv'):
        sys.exit("Not a CSV file ")
    # valid filename
    inFileName = sys.argv[1]
    return(inFileName)

if __name__ == "__main__":
    main()
