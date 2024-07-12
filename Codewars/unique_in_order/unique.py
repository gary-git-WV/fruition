def unique_in_order(sequence):
# From CodeWars 'Unique In Order' Python Kata
# Takes as argument a sequence and returns a list of items without any 
# elements with the same value next to each other and preserving the 
# original order of elements. 
# Elements can be upper case or lower case alpha, or numeric. 
    myseq = sequence
    unique_list = []
    for i in myseq:
        if len(myseq) == 1:
            unique_list.append(myseq[0])
            break
        if myseq[0] == myseq[1]:
            myseq = myseq[1:]
        else:
            unique_list.append(myseq[0])
            myseq = myseq[1:]
    return unique_list