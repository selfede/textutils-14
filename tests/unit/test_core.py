import textutils.core as c

def test_unique_words_basic():
    # Distinct, case-insensitive words sorted alphabetically
    text = "Red blue RED green"
    assert c.unique_words(text) == ["blue", "green", "red"]

def test_unique_words_punctuation():
    # Ignores punctuation and returns only valid words
    text = "Hello, hello! world..."
    assert c.unique_words(text) == ["hello", "world"]

def test_basic_collapse():
    # covers duplicate skipping (True branch)
    assert c.collapse_duplicates("heeellooo", "e") == "hellooo"

def test_no_duplicates():
    # covers normal flow (False branch)
    assert c.collapse_duplicates("hello", "x") == "hello"

def test_empty_string():
    # covers edge case: empty input
    assert c.collapse_duplicates("", "a") == ""

