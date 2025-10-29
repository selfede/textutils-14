import string
from textutils import core as c

def test_basic_removal():
    #Test case with special character
    assert c.remove_punctuation("Hello, world!") == "Hello world"

def test_no_punctuation():
    #Test case with a normal string
    assert c.remove_punctuation("Hello world") == "Hello world"

def test_remove_punctuation_only_punctuation():
    #Tests when their is only punctuation in the string
    text = "!!!???..."
    result = c.remove_punctuation(text)
    assert result == ""