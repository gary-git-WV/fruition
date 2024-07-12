def likes(names):
    # Submission 1 for CodeWars Python Kata "Who likes it??"
    # "Implement the function which takes an array containing 
    # the names of people that like an item. It must return 
    # the display text as shown in the examples:
    # []                                -->  "no one likes this"
    # ["Peter"]                         -->  "Peter likes this"
    # ["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
    # ["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
    # ["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"
    # Note: For 4 or more names, the number in "and 2 others" simply increases.

    if len(names) == 0:
        return("no one likes this")
    elif len(names) == 1:
        text = f"{names[0]} likes this"
        return(text)
    elif len(names) == 2:
        text = f"{names[0]} and {names[1]} like this"
        return(text)
    elif len(names) == 3:
        text = f"{names[0]}, {names[1]} and {names[2]} like this"
        return(text)
    else:
        text = f"{names[0]}, {names[1]} and {(len(names) - 2)} others like this"
        return(text)