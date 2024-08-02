'''Solution attempt to CS50P Week 3 PSet 3 Fuel Gage'''
def main():
    xy = get_input("Fraction:")
    percentage = convert(xy)
    print(gauge(percentage))


def gauge(percentint):
    if 0 <= percentint <=1:
        return("E")
    elif percentint == 99 or percentint == 100:
        return("F")
    elif percentint > 100:
        raise ValueError
    else:
        return(f"{percentint}%")

def get_input(prompt):
    while True:
        # Input a fraction
        infrac = input(prompt)
        return infrac

def convert(infrac):
        # Convert fraction to string
        while True:
            #try:
                instr = infrac.split("/")
            #except (ValueError,TypeError):
                #continue
            #try:
                x = int(instr[0])
            #except (ValueError, TypeError):
                #continue
            #try:
                y = int(instr[1])
            #except (ValueError, TypeError):
                #continue
            if x > y:
                continue
            elif y == 0:
                raise ZeroDivisionError
            #else:
                #continue
            percent = int((round((x / y),2) * 100))
            return percent

if __name__ == "__main__":
    main()
