# CodeWars Split Strings Kata

# Split the string into pairs of two characters. 
# If the string contains an odd number of 
# characters, replace the missing second character of the # # final pair with an underscore ('_').
# Examples: 'abc' =>  ['ab', 'c_'] ... 'abcdef' => ['ab', 'cd', 'ef']

def solution(s):
    
    pairs = []
    if len(s) < 1:
        return pairs
        quit
    while len(s) > 1:
        pairs.append(s[:2])
        s = s[2:]
    if len(s) == 1:
        s += '_'
        pairs.append(s)
    return pairs