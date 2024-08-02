from  bank import value


def test_vowels():
    assert value("aeiou") == 100
def test_numbers():
    assert value("31415") == 100
def test_Hello():
    assert value("Hello")  == 0
def test_startwithh():
    assert value("hardware") == 20
def test_Hello():
    assert value("Hello") == 0
def test_HELLO():
    assert value("HELLO") == 0
def test_HeLlO():
    assert value("HeLlO") == 0
def test_hello():
    assert value("hello") == 0
def test_reallylongstring():
    assert value("Heck of a way to do things") == 20

