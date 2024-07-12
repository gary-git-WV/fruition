def persistence(n):
    # my code
    return
    
n = 19
cntr = 0
digits = list(str(n))
print("Line 8 digits: ", digits)
product = int(digits.pop(0))

def dothemath(digits,product):
    print("Line 12 digits: ", digits, " cntr: ", cntr, " product: ", product)
    
    digit = product 
    product *= digit
    digit = int(digits.pop(0))
    print("Line 16 digit: ", digit, "digits: ", digits, " cntr: ", cntr, " product: ", product)
    return digits, product
    
print("Line 20 product: ", product, "digits: ", digits, "Cntr: ", cntr)    
while len(digits)>0:
    cntr += 1
    print("Line 23 digits ", digits, "cntr: ", cntr)
    dothemath(digits,product)

print("Line 24 Persistence: ", cntr)
print(("Line 25 "), (digits), type(digits), ("product: ", product), ( "cntr: ", cntr))