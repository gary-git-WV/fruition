import random
import sys


def main():
    # Get # of digits in addends
    n = get_level()

    #track score
    score = 0
    # present 10 problems
    for tryprob in range(10):
        problem, solution = get_problems(n)
        # three tries to get each answer right
        tries = 0
        while tries < 3:
            try:
                answer = int(input(problem))
            except ValueError:
                print("EEE")
                tries += 1
                continue
            if int(answer) != int(solution):
                print("EEE")
                tries += 1
                continue
            elif int(answer) == int(solution):
                score += 1
                tryprob += 1
                break
        if tries == 3:
            tryprob += 1
            print(f"{problem}{solution}")
    print("Score:", score)

def get_problems(n):
    # Generate equation and solution
    # Get random numbers of correct length
    x = int(generate_integer(n))
    y = int(generate_integer(n))
    # Generate equation and solution
    problem = (f"{x} + {y} = ")
    solution = (x+y)
    # return  problem and answer
    return(problem, solution)

def get_level():
    # Prompt for a 'level' which will be
    # the number of digits in addends
    while True:
        try:
            n = int(input("Level:"))
        except(ValueError):
            continue
        if n == 1 or n == 2 or n == 3:
            return(n)
        else:
            continue


def generate_integer(level):
    # Generate random number of length level
    if level == 1:
        rnum = random.randrange(0,10)
    elif level == 2:
        rnum = random.randrange(10,100)
    elif level == 3:
        rnum = random.randrange(100,1000)
    else:
        raise ValueError("Value Error")
    return rnum

if __name__ == "__main__":
    main()
