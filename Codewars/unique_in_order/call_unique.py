# This calls my latest CodeWars kata with test cases
# and prints the results.

from unique import unique_in_order
print(unique_in_order('AAAABBBCCDAABBB'))
print(unique_in_order('ABBCcAD'))
print(unique_in_order([1, 2, 2, 3, 3]))
print(unique_in_order((1, 2, 2, 3, 3)))
print(unique_in_order(""))
print(unique_in_order([]))
print(unique_in_order(()))
print(unique_in_order("A"))
print(unique_in_order(["A"]))
print(unique_in_order(("A",)))
print(unique_in_order("AA"))
print(unique_in_order("ABBCcA"))
print(unique_in_order([1, 2, 3, 3, -1]))
print(unique_in_order(["a", "b", "b", "a"]))
