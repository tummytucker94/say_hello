from src.functions.greetings import say_hello

def test_say_hello_with_expected_input():
    result = say_hello("Jermaine")
    assert result == "Hello Jermaine!"

def test_say_hello_with_blank_space():
    result = say_hello(" ")
    assert result == "Hello there!"

def test_say_hello_with_no_space():
    result = say_hello("")
    assert result == "Hello there!"