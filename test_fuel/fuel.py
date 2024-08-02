'''Solution attempt to CS50P Week 3 PSet 3 Fuel Gage'''
def main():
    xy = get_input("Fraction:")
    percentage = convert(xy)
    print(gauge(percentage))

def get_input(prompt):
    while True:
        # Input a fraction
        infrac = input(prompt)
        return infrac

def convert(infrac):
        # Convert fraction to string
        while True:
            instr = infrac.split("/")
            try:
                x = int(instr[0])
            except:
                raise ValueError("numerator must be int")
            y = instr[1]
            if y == '0':
                raise ZeroDivisionError("cannot divide by zero")
            try:
                y = int(instr[1])
            except:
                raise ValueError("denominator must be int")
            if x > y:
                continue
            percent = int((round((x / y),2) * 100))
            return percent

def gauge(percentint):
    intpercent = int(percentint)
    if 0 <= intpercent <=1:
        return("E")
    elif intpercent == 99 or intpercent == 100:
        return("F")
    elif intpercent > 100:
        raise ValueError
    else:
        return(f"{intpercent}%")

if __name__ == "__main__":
    main()
