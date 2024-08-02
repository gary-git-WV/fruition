''' Solution for Harvard CS50P Week 3 PSet 3 Felipe's Taqueria'''
def main():
    # menu in a dictionary
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    total = 0
    while True:
        try:
            item = input("Item: ").title()
        except EOFError:
            break
        if item in menu:
            itemcost = menu.get(item)
            total += float(itemcost)
            print(f"Total: ${total:.2f}")
        else:
            continue

main()
