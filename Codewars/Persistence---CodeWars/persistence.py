def persistence(n):
    #My code begins here
    #Functions to return the persistence of a number

    def multiply(digits1):
        product1 = 1
        while len(digits1) > 0:
            mult = int(digits1.pop(0))
            product1 *= mult
        product1 = list(str(product1))
        return (product1)

    def digify(alist):
        count = 0
        newlist = []
        while len(alist) > 0:
            newlist.append(alist.pop(count))
        return newlist

    if n < 10:
        return 0
        quit()
    digits = list(str(n))
    persistence1 = 1
    while len(digits) > 0:
        product = multiply(digits)
    product = digify(product)
    while len(product) > 1:
        persistence1 += 1
        product = multiply(product)
    return persistence1