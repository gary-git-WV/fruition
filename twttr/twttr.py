def main():
    vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u' ,'U']
    instring = input("Input: ")
    for char in instring:
        if char in vowels:
            instring = instring.replace(char, "")
    print("Output:", instring)

main()

