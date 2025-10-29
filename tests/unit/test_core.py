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

def test_basic_lowercase():
    #testing for basic lowercase vowels
    assert c.count_vowels("good morning") == 4

def test_mixed_case():
    #testing for mixed case vowels
    assert c.count_vowels("AEiou") == 5

def test_punctuation_and_numbers_are_ignored():
    #testing that punctuation and numbers are ignored
    assert c.count_vowels("P3, brrr!") == 0

def test_slugify_basic():
    #testing basic slugify    
    text = "Hello World"
    assert c.slugify(text) == "hello-world"

def test_slugify_removes_special_characters():
    #testing slugify with special characters    
    text = "Fast & Furious: Tokyo Drift!"
    assert c.slugify(text) == "fast-furious-tokyo-drift"

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

def average_test_simple_words():
    # this fucntion tests with simple words
    result = c.average_word_length("python git")
    assert result == 4.5

def average_test_different_lengths():
    # Test with different word lengths: "I" (1) + "love" (4) + "Python" (6) = 11 / 3 = 3.67
    result = c.average_word_length("good job team")
    assert result == 3.67

def average_test_only_punctuation():
    # Test with only punctuation: should return 0.0
    result = c.average_word_length("!@#$%^&*()")
    assert result == 0.0
