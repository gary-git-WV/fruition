'''Solution for Exercism Python exercise "Rotational Cipher"'''
# using string for filling alphabets
import string
def rotate(text, key):
    '''First, initialize strings of alpha characters'''
    string_lower = string.ascii_lowercase
    string_upper = string.ascii_uppercase
    # Initialize empty string for return string
    cipher_string = ''
    # Cycles through the end of the alpha string
    if key > 25:
        key -= 26
    for letter in text:
        if letter in string_lower:
            offset = string_lower.find(letter) + key
            if offset > 25:
                offset -= 26
            new_letter = string_lower[offset]
        elif letter in string_upper:
            offset = string_upper.find(letter) + key
            if offset > 25:
                offset -= 26
            new_letter = string_upper[offset]
        # Don't shift numbers or whitespaces
        else:
            new_letter = letter
        cipher_string = cipher_string + new_letter
    return cipher_string
