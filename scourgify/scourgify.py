''' Expects the user to provide two command-line arguments:
        the name on an existing CSV file to read as input, whose columns
        are assumed to be, in order, name and house, and the name of a new
        CSV to write as output, whose columns should be, in order, first,
        last, and house. ___ Converts that input to that output, splitting
        each name into a first name and last name. Assume that each student
        will have both a first name and last name. ___  If the user does not
        provide exactly two command-line arguments, or if the first cannot
        be read, the program should exit via sys.exit with an error message.'''
import sys
import csv

def main():
    filenames = getinput()
    infilename = filenames[0]
    outfilename = filenames[1]
    if infilename == 0:
        sys.exit
    if outfilename == 0:
        sys.exit
    mages = readfile(infilename)
    writefile(mages, outfilename)
    return 0

def readfile(infilename):
    # initialize temporary list
    last = []
    first = []
    mages = []
    names = []
    # get data from file
    with open(infilename) as file:
        magereader = csv.DictReader(file)
        for mage in magereader:
            # swap positions of first and last names
            house =  mage.get("house")
            lastfirst = mage.get("name")
            names = lastfirst.split(", ")
            last = names[0]
            first = names[1]
            # create dictionary for each student
            mage = {"first": first, "last": last, "house": house}
            # add dictionary to list
            mages.append(mage)
    print("Line 21: mages: ", mages, "type(mages): ", type(mages))
    return mages

def getinput():
    # input must include 2 filename arguments
    # (one file to read from, one file to write to)
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments ")
    elif len(sys.argv) > 3:
         sys.exit("Too many command-line arguments ")
    infilename = sys.argv[1]
    outfilename = sys.argv[2]
    # first file must exist
    try:
        file = open(infilename)
    except FileNotFoundError:
        sys.exit(f"Could not read {infilename}")
    file.close()
    # files must be  a CSV files
    if not sys.argv[1].endswith('csv'):
        sys.exit("Not a CSV file ")
    # valid filename
    
    return(infilename, outfilename)

def writefile(mages, outfilename):
    # create csv file and add headers to it
    with open(outfilename, 'w', newline='') as csvfile:
        fieldnames = ['first', 'last', 'house']
        magewriter = csv.writer(csvfile)
        magewriter.writerow(['first'] + ['last'] + ['house'])
        # assemble student info and write to file
        for mage in mages:
            first = mage.get('first')
            last = mage.get('last')
            house = mage.get('house')
            mageinfo = [first, last, house]
            magewriter.writerow(mageinfo)
    return 0

if __name__ == "__main__":
    main()
