import re
def unique_words(text: str):
    text = text.lower()
    words = re.findall(r'\b[a-z0-9]+\b', text)
    unique = sorted(set(words))
    return unique


    