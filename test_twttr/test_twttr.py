from twttr import shorten


def test_vowels():
    assert shorten("Abracadabra") == "brcdbr"
def test_numbers():
    assert shorten("1 and 2 and 3") == "1 nd 2 nd 3"
def test_punctuation():
    assert shorten("Trains, not planes, nor automobiles.")  == "Trns, nt plns, nr tmbls."
def test_rndmcaps():
    assert shorten("OnCe UpOn A MiDnIgHt dReArY") == "nC pn  MDngHt dRrY"
