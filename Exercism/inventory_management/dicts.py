"""Functions to keep track and alter inventory."""
# Exercism "Inventory Management" exercise for Python

# Task 1
def create_inventory(items):
    ''' Create a dict that tracks the amount (count) of each element on the `items` list.
    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.'''
    inventory = {}
    count = 1
    index = 0
    while index < (len(items)-1):
        if items[index] == items[index+1]:
            count += 1
            index += 1
        else:
            inventory.update({items[index]: count})
            count = 1
            index += 1
    inventory.update({items[index]: count})
    return inventory

# Task 2
def add_items(inventory, items):
    ''' Add or increment items in inventory using elements from the items `list`.
    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.'''
    count = 1
    index = 0
    while index < (len(items)):
        if items[index] in inventory.keys():
            inventory[items[index]] = inventory[items[index]] + 1
        else:
            inventory.update({items[index]: count})
        if index < len(items):
            count = 1
            index += 1
    return inventory

# Task 3
def decrement_items(inventory, items):
    ''' Decrement items in inventory using elements from the `items` list.
     :param inventory: dict - inventory dictionary.
     :param items: list - list of items to decrement from the inventory.
     :return: dict - updated inventory with items decremented.'''
    index = 0
    while index < (len(items)):
        if items[index] in inventory.keys():
            if inventory[items[index]] > 0:
                inventory[items[index]] = inventory[items[index]] - 1
        if index < len(items):
            index += 1
    return inventory

# Task 4
def remove_item(inventory, item):
    ''' Remove item from inventory if it matches `item` string.
     :param inventory: dict - inventory dictionary.
     :param item: str - item to remove from the inventory.
     :return: dict - updated inventory with item removed. 
     Current inventory if item does not match.'''
    if item in inventory.keys():
        inventory.pop(item)
    return inventory

# Task 5
def list_inventory(inventory):
    ''' Create a list containing only available (item_name, item_count > 0) pairs in inventory.
     :param inventory: dict - an inventory dictionary.
     :return: list of tuples - list of key, value pairs from the inventory dictionary.'''
    inventory2 = inventory.copy()
    for item in inventory:
        if inventory[item] < 1:
            inventory2.pop(item)
    listinv = list(inventory2.items())
    listinv.sort()
    return listinv
