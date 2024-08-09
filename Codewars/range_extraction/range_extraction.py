'''A format for expressing an ordered list of integers is to use a comma 
separated list of either individual integers or a range of integers denoted 
by the starting integer separated from the end integer in the range by a 
dash, '-'. The range includes all integers in the interval including both 
endpoints. It is not considered a range unless it spans at least 3 numbers. 
For example "12,13,15-17" . Complete the solution so that it takes a list of 
integers in increasing order and returns a correctly formatted string in the 
range format.  Example:

solution([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15,
 17, 18, 19, 20])
returns "-10--8,-6,-3-1,3-5,7-11,14,15,17-20"'''

def main():
    output = solution([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
    print("Output: ", output)


def solution(args):
    outstring = ""
    index, start, stop = 0, 0, 1
    while index in range(len(args)):
        while True:
            if stop >= len(args):
                break
            if args[index] - args[stop] == -1:
                index += 1
                stop += 1
            else:
                break    
        if stop - start == 1:
            outstring = outstring + str(args[start]) + ","
        elif stop - start == 2:
            outstring = outstring + str(args[start]) + "," + str(args[stop-1]) + ","
        elif stop >= len(args):
            outstring = outstring + str(args[start]) + "-" + str(args[stop-1])
            break
        else: 
            outstring = outstring + str(args[start]) + "-" + str(args[stop-1]) + ","
        index = stop
        start = index
        stop = index + 1
    if outstring.endswith(","):
        outstring = outstring[0:-1]    
    return(outstring)

if __name__ == "__main__":
    main()
