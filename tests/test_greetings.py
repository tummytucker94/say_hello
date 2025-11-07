from src.functions.greetings import say_hello
import time

def test_say_hello_with_typical_name():
    result = say_hello("Jermaine")
    assert result == "Hello Jermaine!"

def test_say_hello_with_alternate_name():
    result = say_hello("Maria")
    assert result == "Hello Maria!"

def test_say_hello_with_space_only():
    result = say_hello(" ")
    assert result == "Hello there!"

def test_say_hello_with_blank_input():
    result = say_hello("")
    assert result == "Hello there!"

def test_say_hello_with_long_name():
    result = say_hello("Supercalifragilisticexpialidocious")
    assert result == "Hello Supercalifragilisticexpialidocious!"

def test_say_hello_is_fast():
    start = time.perf_counter()

    # call it a bunch of times to smooth out noise
    for _ in range(1000):
        say_hello("Jermaine")

    end = time.perf_counter()
    duration = end - start

    # assert total time stays under 1 second
    assert duration < 1.0, f"Too slow: {duration:.6f} seconds"