def main():
    greeting = input("Greet me, please: ").lower().strip()
    if greeting[:5] == "hello":
        print("$0")
    elif greeting[:1] == "h":
        print("$20")
    else:
        print("$100")

main()
