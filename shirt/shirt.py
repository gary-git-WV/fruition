'''Expects exactly two command-line arguments: in sys.argv[1], the name
    (or path) of a JPEG or PNG to read (i.e., open). As input in
    sys.argv[2], the name (or path) of a JPEG or PNG to write (i.e., save)
     as output. The program should then overlay shirt.png (which has a
    transparent background) on the input after resizing and cropping the
    input to be the same size, saving the result as its output.'''
import os.path
import sys
from PIL import Image, ImageOps

def main():
    # call function to get filenames from CLI
    filenames = getinput()
    infile = filenames[0]
    infilename = filenames[1]
    outfile = filenames[2]
    outfileext = filenames[3]
    if infile == 0:
        sys.exit
    if outfile == 0:
        sys.exit
    # get info about shirt.png
    shirt = "shirt.png"
    with Image.open("shirt.png") as img:
        shirtsize = img.size
    # resize input file, paste in shirt, and create output file
    with Image.open(infile) as img1, Image.open('shirt.png') as img2:
        img3 = ImageOps.fit(img1, shirtsize)
        img3.paste(img2,img2)
        img3.save(outfile)
    return 0

def getinput():
    # file name validation
    # input must include 2 filename arguments
    # (one file to read from, one file to write to)
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments ")
    elif len(sys.argv) > 3:
         sys.exit("Too many command-line arguments ")
    infilename = sys.argv[1]
    outfilename = sys.argv[2]
    # input file must exist
    try:
        file = open(infilename)
    except FileNotFoundError:
        sys.exit(f"Input does not exist")
    file.close()
    # files must be same type
    infileext, outfileext = getextensions(infilename, outfilename)
    if infileext.lower() != outfileext.lower():
        sys.exit("Input and output have different extensions")
    # input file must be jpg or jpeg or png
    if outfileext.lower() == '.jpg':
        pass
    elif outfileext.lower() == '.jpeg':
        pass
    elif outfileext.lower() == '.png':
        pass
    else:
        sys.exit("Invalid output")
    # valid filename
    return(infilename, infileext, outfilename, outfileext)

def getextensions(inf, outf):
    # get and store file types
    insplit = os.path.splitext(inf)
    infileext = insplit[1]
    outsplit = os.path.splitext(outf)
    outfileext = outsplit[1]
    return(infileext, outfileext)

if __name__ == "__main__":
    main()
