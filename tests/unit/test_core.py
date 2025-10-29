import textutils.core as c
def test_basic_lowercase():
    assert c.count_vowels("good morning") == 4

def test_mixed_case():
    assert c.count_vowels("AEiou") == 5

def test_punctuation_and_numbers_are_ignored():
    assert c.count_vowels("P3, brrr!") == 0
