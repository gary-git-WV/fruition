def main():
    userstr = input("Please enter some stuff: ")
    print(convert(userstr))

def convert(instr):
    outstr = instr.replace(":)", "🙂").replace(":(", "🙁")
    return outstr

main()

