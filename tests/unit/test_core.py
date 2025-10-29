import textutils.unique_words as c

def test_unique_words_basic():
    # Distinct, case-insensitive words sorted alphabetically
    text = "Red blue RED green"
    assert c.unique_words(text) == ["blue", "green", "red"]

def test_unique_words_punctuation():
    # Ignores punctuation and returns only valid words
    text = "Hello, hello! world..."
    assert c.unique_words(text) == ["hello", "world"]