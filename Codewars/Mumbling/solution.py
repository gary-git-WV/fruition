'''Convert string to incremented hyphenated capitalized string'''
def accum(st):
    # The function that Does The Magic
    queue = ''
    # There's a hidden elephant trap in this problem
    charindex = 0
    while charindex < len(st):
        char = st[charindex]
        temp = ''
        count = 1
        index = (charindex + 1)
        while count <= index:
            temp += st[charindex]
            count += 1
        index += 1
        if index <= len(st):
            queue += temp.capitalize() + '-'
        else:
            queue += temp.capitalize()
        charindex += 1
    return queue
