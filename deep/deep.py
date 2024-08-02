def main():
    answer = input("What is the answer to the Great Question of Life, The Universe, and Everything?")
    usable = answer.lower().strip()
    return decide(usable)

def decide(words):
    match words:
        case "forty two" | "forty-two" | "42":
            print("Yes")
        case _:
            print("No")

main()
