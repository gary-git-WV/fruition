'''This is my, erm, "solution", for Codewars 4 kyu kata "The observed PIN."
    I normally place my lib import headers outside and before all func defs,
    but in this case, I was only submitting the get_pins() function, so 
    I did it, like so:'''
 
def main():
    print(get_pins(369))    
    
def get_pins(observed):
    from itertools import product
    pindict = {1: [1,2,4], 2: [2,1,3,5], 3: [3,2,6], 4: [4,1,5,7], 
               5: [5,2,4,6,8], 6: [6,3,5,9], 7: [7,4,8], 
               8: [8,5,7,9,0], 9: [9,6,8], 0: [8,0]}
    outlist = []
    supply = []
    for digit in str(observed):
        supply.append(pindict.get(int(digit)))
    list1=list(product(*supply))
    for tupl in range(len(list1)):
        temp = ""
        for digit in list1[tupl]:
            temp = temp + str(digit)
        temp = temp.replace(",","")
        temp = temp.replace(" ","")
        outlist.append(temp)
    return outlist
if __name__ == "__main__":
    main()
