from bank2 import value

def testing():
    assert value("what's up") == "$100"
    assert value("nice to see you") == "$100"
    assert value("hello") == "$0"
    assert value("Hello") == "$0"
    assert value("Hi") == "$20"
    assert value("heyy") == "$20"
