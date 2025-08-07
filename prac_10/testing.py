"""Prac 10 - Testing, assert and doctest."""

import doctest


def repeat_string(string, n):
    """Repeat string n times, for example:
    >>> repeat_string("hi", 2)
    'hihi'
    """
    return string * n


def is_long_word(word, length=5):
    """Determine if the word is as long or longer than the given length.
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def phrase_to_sentence(phrase):
    """Convert a phrase to a sentence: capitalised and ending with a single period.
    >>> phrase_to_sentence("hello")
    'Hello.'
    >>> phrase_to_sentence("It is sunny.")
    'It is sunny.'
    >>> phrase_to_sentence("what time is it")
    'What time is it.'
    """
    phrase = phrase.strip()
    if not phrase.endswith('.'):
        phrase += '.'
    return phrase[0].upper() + phrase[1:]


class Car:
    """Car class for testing."""

    def __init__(self, fuel=0):
        self.fuel = fuel


# Write assert statements to test the Car class's fuel attribute
def test_car():
    car = Car()
    assert car.fuel == 0, "Default fuel should be 0"
    car2 = Car(50)
    assert car2.fuel == 50, "Fuel should be set to 50"


doctest.testmod()
