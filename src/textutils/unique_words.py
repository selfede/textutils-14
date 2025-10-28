import re
def unique_words(text: str):
    """
    Return a sorted list of unique, case-insensitive words from the text.
    """
    text = text.lower()
    words = re.findall(r'\b[a-z0-9]+\b', text)


    