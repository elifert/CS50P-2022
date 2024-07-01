from twttr2 import shorten

def test_shorten():
    assert shorten("elif") == "lf"
    assert shorten("Elif") == "lf"