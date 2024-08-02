import inflect

def main():
    p = inflect.engine()
    namelist=[]
    while True:
        try:
            newname = input("Name: ")
        except(EOFError):
             break
        else:
            namelist.append(newname)
    names = p.join(namelist)
    print(f"Adieu, adieu, to {names}.")

if __name__ == "__main__":
    main()
