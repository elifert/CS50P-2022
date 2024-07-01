from numb3rs import validate

def testing():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.0") == True
    assert validate("275.3.6.28") == False
    assert validate("cat") == False
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False
    assert validate("122.255.12.0") == True
    assert validate("30.0.39.57") == True
    assert validate("255.256.29.33") == False