import listfiltering
# My first real effort at passing data between modules.
# It was either this, or dive into the pytest rabbit hole,
# to which I do not feel ready to commit just yet.

list1 = [1, 2, 'a', 'b'] 
list2 = [1, 'a', 'b', 0, 15] 
list3 = [1, 2, 'aasf', '1', '123', 123]
mylist = [list1, list2, list3]
for item in mylist:
    testlist1 = listfiltering.filter_list(item)
    print(testlist1)