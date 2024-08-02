def main():
    import emoji
    # emoji.emojize(language='alias')
    instring = input("Input: ")
    print(type(instring))
    print(emoji.emojize(instring, language='alias'))

main()
