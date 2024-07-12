def filter_list(l):
    # Return a new list with the strings filtered out.
    
    l2 = []
    for i in range(len(l)):
        if type(l[i]) == int:
            l2.append(l[i])
    return l2