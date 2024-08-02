'''Solution attempt to CS50P Week 3 PSet 3 Fuel Gage'''
def main():
    x, y = get_input("Fraction:")
    try:
        percent = int((round((x / y),2) * 100))
    except (ValueError, ZeroDivisionError):
        pass
    if 0 <= percent <=1:
        print("E")
    elif percent == 99 or percent == 100:
        print("F")
    elif percent > 100:
        pass
    else:
        print(percent, "%", sep="")

def get_input(prompt):
    while True:
        # Input a fraction
        infrac = input(prompt)
        # Convert fraction to string
        try:
            instr = infrac.split("/")
        except (ValueError,TypeError):
            continue
        try:
            x = int(instr[0])
        except (ValueError, TypeError):
            continue
        try:
            y = int(instr[1])
        except (ValueError, TypeError):
            continue
        if x > y:
            continue
        elif y == 0:
            continue
        else:
            return x, y

main()
