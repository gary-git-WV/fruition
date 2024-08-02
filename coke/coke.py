def main():
    due = 50
    while due > 0:
        coin = get_coin()
        due = the_math(due, coin)
        if due <= 0:
            print("Change Owed:", due * (-1))
        else:
            print("Amount Due:", due)

def get_coin():
    coin = int(input("Insert Coin:"))
    if coin == 25:
        return coin
    elif coin == 10:
        return coin
    elif coin == 5:
        return coin
    else:
        return 0

def the_math(due, coin):
    due -= coin
    return due

main()
