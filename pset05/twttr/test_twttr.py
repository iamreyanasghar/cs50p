from twttr import shorten


''' Testing shorten() from twttr.py '''

# testing vowels
def test_vowels():
    assert shorten("AEIOU") == ""
    assert shorten("aeiou") == ""


# testing upper case
def test_upper():
    assert shorten("REYAN") == "RYN"
    assert shorten("ASGHAR") == "SGHR"


# testing lower case
def test_lower():
    assert shorten("name") == "nm"
    assert shorten("computer") == "cmptr"


# testing numbers & punctuation
def test_numbers_punctuation():
    assert shorten("CS50") == "CS50"
    assert shorten("Wow!") == "Ww!"
