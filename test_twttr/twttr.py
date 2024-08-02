'''Solution for CS50 PSet 5
"Testing my twttr"'''
def main():
    # Get input string
    instring = input("Input: ")
    # Call shorten function, print result
    print(shorten(instring))


def shorten(word):
    vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u' ,'U']
    for char in word:
        if char in vowels:
            word = word.replace(char, "")
    return word

if __name__ == "__main__":
    main()
