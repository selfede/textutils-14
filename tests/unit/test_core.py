from textutils.count_vowels import count_vowels
def test_basic_lowercase():
    assert count_vowels("good morning") == 4

def test_mixed_case():
    assert count_vowels("AEiou") == 5

def test_punctuation_and_numbers_are_ignored():
    assert count_vowels("P3, brrr!") == 0
