from  plates import is_valid


def test_toolongx():
    assert is_valid("TooLong") == False
def test_tooshort():
    assert is_valid("I") == False
def test_numbersfirst():
    assert is_valid("42All") == False
def test_numbersmiddle():
    assert is_valid("Is42It") == False
def test_zerofirst():
    assert is_valid("My042") == False
def test_justright():
    assert is_valid("Ansr42") == True
def test_allnumbers():
    assert is_valid("424242") == False
def test_noalpha():
    assert is_valid("AN$R42") == False



