'''Exercism "House" in Python'''
def recite(start_verse, end_verse):
    # list of the verses
    verses = ["This is ", "the house that Jack built.",
    "the malt that lay in ", "the rat that ate ", "the cat that killed ", 
    "the dog that worried ", "the cow with the crumpled horn that tossed ", 
    "the maiden all forlorn that milked ", 
    "the man all tattered and torn that kissed ", 
    "the priest all shaven and shorn that married ", 
    "the rooster that crowed in the morn that woke ", 
    "the farmer sowing his corn that kept ", 
    "the horse and the hound and the horn that belonged to "]

    verse_index = start_verse
    # queue will build the return list
    queue = []
    def makeaverse(index):
        # generate each individual verse string
        jack = [verses[0]]
        while index >= 1:
            jack.append(verses[index])
            index -= 1
        jack = ''.join(jack)
        return jack

    while verse_index <= end_verse:
        vindex = verse_index
        queue.append(makeaverse(vindex))
        verse_index += 1
    return queue
