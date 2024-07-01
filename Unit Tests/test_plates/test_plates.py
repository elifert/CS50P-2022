from plates2 import is_valid

def test_plates():
    assert is_valid("CS50") == True
    assert is_valid("00000") == False