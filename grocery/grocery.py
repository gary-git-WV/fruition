def main():
    grocery_list = {}

    while True:
        try:
            item = input().upper()
        except EOFError:
            break
        if item in grocery_list:
            x = grocery_list.get(item)
            x += 1
            grocery_list.update({item: x})
        else:
            grocery_list.update({item: 1})
    sorted_list = dict(sorted(grocery_list.items()))
    for i in sorted_list:
        print(sorted_list[i], i)


main()
