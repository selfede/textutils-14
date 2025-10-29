# Textutils Team 14
This is a Text Utilities group assignemnt for the Python for Data Science Class.

## Environmenet Recreation 
### 1. Clone the repository 
`git clone https://github.com/selfede/textutils-14`

`cd textutils-14`

### 2. Recreate the environment using Micromamba 
`micromamba create -f environment.yml -y`

`micromamba activate textutils`

## How to install the package (pip install -e .)
`pip install -e .`

Ensure that the package is installed in editable mode
### Running the Tests 
`pytest -v`

Ensure that 100% of the test have been completed, some utils will have more tests than others.

### Viewing Test Coverage Details 
`pytest --cov`

The coverage for all of the tests should be >=90%

## Implemented Features:
remove_punctuation(text) — strip punctuation while keeping spaces and letters.
count_vowels(text) — count vowels in the given text. 
slugify(text) — convert text to lowercase, hyphen-separated safe string.  
average_word_length(text) — compute mean length of words in text.
unique_words(text) — return a sorted list of distinct words (case-insensitive).  
collapse_duplicates(text, char) — replace runs of the same char with one.  
word_lengths(text) — return a dict mapping words to their lengths.  


## Coverage Report:

Name                                   Stmts   Miss  Cover
----------------------------------------------------------
src/textutils/__init__.py                  0      0   100%
src/textutils/core.py                     55      1    98%
tests/integration/test_end_to_end.py      17      0   100%
tests/unit/test_core.py                   51      0   100%
----------------------------------------------------------
TOTAL                                    123      1    99%
========================================================= 20 passed in 0.04s 


## Team Members
Federica Selvini as selfede

Ivan Salticov as vein134

Florian Nix as floriannix4-stack

Sharath Raveendran as sharathandres51-eng










