import textutils.core as c

def test_simple_words():
    # this tests checks basic words
    result = c.word_lengths("hello world")
    assert result == {"hello": 5, "world": 5}

def test_different_lengths():
    # this function tests for with words of different lengths
    result = c.word_lengths("great work team")
    assert result == {"great": 5, "work": 4, "team": 4}

def test_with_punctuation():
    # this tests that punctuation is included in the word length
    result = c.word_lengths("great work!")
    assert result == {"great": 5, "work!": 5}