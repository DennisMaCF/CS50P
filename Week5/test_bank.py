from bank import value

def test_value():
    assert value("Hello") == 0
    assert value(" Hello ") == 0
    assert value("Hello, Newman") == 0
    assert value("How you doing?") == 20
    assert value("What's happening?") == 100
    assert value("What's up?") == 100
# def test_value():
#     assert value("Hello, world") == "$0"
#     assert value("Hi, world") == "$20"
#     assert value("Bye, world") == "$100"
#     assert value("hello") == "$0"
#     assert value("HELLO") == "$0"
#     assert value("hi") == "$20"
#     assert value("HI") == "$20"

