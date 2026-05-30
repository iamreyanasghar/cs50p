from um import count

def test_words_with_um():
    assert count("yummy") == 0
    assert count("summer") == 0

def test_um():
    assert count("um") == 1
    assert count("um?") == 1
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2
