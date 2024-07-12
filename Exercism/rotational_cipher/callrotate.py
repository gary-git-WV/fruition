'''Call rotate.import.py with 2 args'''
from rotate import rotate

# print(rotate('Testing 1 2 3 testing', 4))
      
      
#     def test_rotate_a_by_0_same_output_as_input(self):
assert rotate("a", 0) == "a"
#    def test_rotate_a_by_1(self):
assert rotate("a", 1) == "b"
#    def test_rotate_a_by_26_same_output_as_input(self):
assert rotate("a", 26) == "a"
#    def test_rotate_m_by_13(self):
assert rotate("m", 13) == "z"
#    def test_rotate_n_by_13_with_wrap_around_alphabet(self):
assert (rotate("n", 13) == "a")
#    def test_rotate_capital_letters(self):
assert rotate("OMG", 5) == "TRL"
#    def test_rotate_spaces(self):
assert rotate("O M G", 5) == "T R L"
#    def test_rotate_numbers(self):
assert rotate("Testing 1 2 3 testing", 4) == "Xiwxmrk 1 2 3 xiwxmrk"   
#    def test_rotate_punctuation(self):
assert rotate("Let's eat, Grandma!", 21) == "Gzo'n zvo, Bmviyhv!"
#    def test_rotate_all_letters(self):
assert rotate("The quick brown fox jumps over the lazy dog.", 13) == "Gur dhvpx oebja sbk whzcf bire gur ynml qbt."
'''Instructions 
    Create an implementation of the rotational cipher, also 
        sometimes called the Caesar cipher.
    The Caesar cipher is a simple shift cipher that relies on transposing all 
        the letters in the alphabet using an integer key between 0 and 26. Using 
        a key of 0 or 26 will always yield the same output due to modular 
        arithmetic. The letter is shifted for as many values as the value of the 
        key.
    The general notation for rotational ciphers is ROT + <key>. The most 
        commonly used rotational cipher is ROT13.
    
    A ROT13 on the Latin alphabet would be as follows:
    Plain:  abcdefghijklmnopqrstuvwxyz
    Cipher: nopqrstuvwxyzabcdefghijklm

    It is stronger than the Atbash cipher because it has 27 possible keys, and
    25 usable keys.

    Ciphertext is written out in the same formatting as the input including 
    spaces and punctuation.
    
    Examples

    ROT5 omg gives trl
    ROT0 c gives c
    ROT26 Cool gives Cool
    ROT13 The quick brown fox jumps over the lazy dog. gives Gur dhvpx oebja sbk whzcf bire gur ynml qbt.
    ROT13 Gur dhvpx oebja sbk whzcf bire gur ynml qbt. gives The quick brown fox jumps over the lazy dog.'''
