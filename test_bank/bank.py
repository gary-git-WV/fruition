def main():
    greeting = input("Greet me, please: ")
    response = value(greeting)
    print(response)

def value(inputS1):
    inputS = inputS1.lower().strip()
    if inputS[:5] == "hello":
        return(int(0))
    elif inputS[:1] == "h":
        return(int(20))
    else:
        return(int(100))

if __name__ == "__main__":
    main()
