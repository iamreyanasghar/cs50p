from plates import is_valid


# must start with at least two letter
def test_start():
    assert is_valid("CS50") == True
    assert is_valid("RNJ125") == True

    # invalid beginnings
    assert is_valid("1CS50") == False
    assert is_valid("C1") == False
    assert is_valid("11") == False

# valid lenght range 2-6
def test_length():
    assert is_valid("RNJ125") == True
    assert is_valid("CS") == True
    assert is_valid("H") == False
    assert is_valid("OUTATIME") == False


# checking numbers
def test_number():
    assert is_valid("CS50P") == False
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False


# checking puntuation
def test_punctuation():
    assert is_valid("PI3.14") == False
    assert is_valid("PI314") == True

