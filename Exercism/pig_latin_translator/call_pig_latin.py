'''Calls module with data '''
from pig_latin import translate
# class PigLatinTest(unittest.TestCase):

# def test_word_beginning_with_a(self):
assert translate("apple") == "appleay"

#def test_word_beginning_with_e(self):
assert translate("ear") == "earay"

#def test_word_beginning_with_i(self):
assert translate("igloo") == "iglooay"

#def test_word_beginning_with_o(self):
assert translate("object") == "objectay"

#def test_word_beginning_with_u(self):
assert translate("under") == "underay"

#def test_word_beginning_with_a_vowel_and_followed_by_a_qu(self):
assert translate("equal") == "equalay"

#def test_word_beginning_with_p(self):
assert translate("pig") == "igpay"

#def test_word_beginning_with_k(self):
assert translate("koala") == "oalakay"

#def test_word_beginning_with_x(self):
assert translate("xenon") == "enonxay"

#def test_word_beginning_with_q_without_a_following_u(self):
assert translate("qat") == "atqay"

#def test_word_beginning_with_ch(self):
assert translate("chair") == "airchay"

#def test_word_beginning_with_qu(self):
assert translate("queen") == "eenquay"

#def test_word_beginning_with_qu_and_a_preceding_consonant(self):
assert translate("square") == "aresquay"

#def test_word_beginning_with_th(self):
assert translate("therapy") == "erapythay"

#def test_word_beginning_with_thr(self):
assert translate("thrush") == "ushthray"

#def test_word_beginning_with_sch(self):
assert translate("school") == "oolschay"

#def test_word_beginning_with_yt(self):
assert  translate("yttria") == "yttriaay"

#def test_word_beginning_with_xr(self):
assert  translate("xray") == "xrayay"

#def test_y_is_treated_like_a_consonant_at_the_beginning_of_a_word(self):
assert  translate("yellow") == "ellowyay"

#def test_y_is_treated_like_a_vowel_at_the_end_of_a_consonant_cluster(self):
assert  translate("rhythm") == "ythmrhay"

#def test_y_as_second_letter_in_two_letter_word(self):
assert  translate("my") == "ymay"

#def test_a_whole_phrase(self):
assert  translate("quick fast run") == "ickquay astfay unray"
