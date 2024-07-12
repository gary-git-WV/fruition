'''Calls functions from dicts.py, passing appropriate args'''
from dicts import create_inventory, add_items, decrement_items, remove_item
from dicts import list_inventory
# Task 1
print(create_inventory(["coal", "wood", "wood", "diamond", "diamond", "diamond"]))

# Task 2
print(add_items({"coal":1}, ["wood", "iron", "coal", "wood"]))
# expected ({"coal":2, "wood":2, "iron":1})


# Task 3
print(decrement_items({"coal":2, "wood":1, "diamond":2},
                       ["coal", "coal", "wood", "wood", "diamond"]))


# Task 4
print(remove_item({"coal":2, "wood":1, "diamond":2}, "gold"))


# Task 5
print(list_inventory({"coal":7, "wood":11, "diamond":2, "iron":7, "silver":0}))
