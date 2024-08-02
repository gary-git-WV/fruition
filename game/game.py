import random

def gen_num(prompt):
    while True:
        try:
            q = int(input(f"{prompt}"))
        except(ValueError):
            continue
        if q <= 0:
            continue
        else:
            return q

def main():
    # Prompt for input positive integer n
    n = gen_num("Level: ")

    # Generate random number between 1 and n
    try:
        n2 = random.randrange(1,n)
    except(ValueError):
        if n == 1:
            n2 = 1
    # Prompt for a guess
    while True:
        g1 = gen_num("Guess: ")
        if g1 < n2:
            print("Too small!")
        elif g1 > n2:
            print("Too large!")
        else:
            print("Just right!")
            break

if __name__ == "__main__":
    main()
