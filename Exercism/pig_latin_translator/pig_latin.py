'''Solution for Exercism Pig Latin Python exercise'''
def translate(text):
    '''Translates text to "pig latin" '''
    words = text.lower() #make copy of text, convert to lowercase
    words = words.split() #make list from string 'text'
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxz'
    for x in words: # Step through each item in list
        word = str(x)
        if word[0] in vowels: #Rule 1
            word1 = word + 'ay'
        elif (word[:2] == 'xr') or (word[:2] =='yt'): #Rule 1
            word1 = word + 'ay'
        elif word[0] == 'y': # Rule 4
            word1 = word[1:] + word[0] + 'ay'
        elif 'qu' in word[:3]: # Rule 3
            i = word.rindex('qu')
            word1 = word[i + 2:] + word[:i + 2]+'ay'
        else:
            word1 = word
            while word1[0] in consonants: # Rule 2
                word1 = word1[1:] + word1[0]
            word1 = word1 + 'ay'
        text = text.replace(word, word1)
    return text
