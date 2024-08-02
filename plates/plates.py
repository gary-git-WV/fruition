def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")
    # Solution for CS50P Week 2 PSet 2
    # "Vanity Plates"

def is_valid(s):
    # max 6 chars min 2 chars
    if len(s) > 6:
        return False
    elif len(s) < 2:
        return False
    # can't have periods, spaces or punctuation
    elif not(s.isalnum()):
        return False
    # must start weith at least 2 letters
    elif not((s[0:2]).isalpha()):
        return False
    # numbers must come at the end, not in the middle
    # init a negative index, check that no letter
    # is preceeded by a number
    # initialize negative index
    ni = -1
    while ni > len(s)*(-1):
        if (s[ni]).isalpha():
            if (s[ni-1]).isnumeric():
                return False
        ni -= 1
    # zero cannot preceed other numbers
    i = 2
    while i < (len(s)-1):
        if (s[i]) == '0':
            if (s[i+1]).isnumeric():
                return False
        i += 1
    return True
main()
