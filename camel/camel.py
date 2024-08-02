def main():
    instring = input("camelCase: ")
    for c in range(len(instring)-1):
        if instring[c].isupper():
            instring = instring.replace(instring[c], ("_" + instring[c].lower()))

    print("snake_case: ", instring)

main()
