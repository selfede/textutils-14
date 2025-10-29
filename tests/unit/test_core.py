import textutils.core as c

def test_simple_words():
    # this fucntion tests with simple words
    result = c.average_word_length("python git")
    assert result == 4.5

def test_different_lengths():
    # Test with different word lengths: "I" (1) + "love" (4) + "Python" (6) = 11 / 3 = 3.67
    result = c.average_word_length("good job team")
    assert result == 3.67

def test_only_punctuation():
    # Test with only punctuation: should return 0.0
    result = c.average_word_length("!@#$%^&*()")
    assert result == 0.0