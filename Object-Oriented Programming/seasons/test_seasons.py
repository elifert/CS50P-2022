from seasons import get_age

def test_age():
    assert get_age("2005-03-12") == "Nine million, nine hundred forty-three thousand, two hundred minutes"
    assert get_age("2005-01-26") == "Ten million, eight thousand minutes"
