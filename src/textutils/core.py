import re
def unique_words(text: str):
    text = text.lower()
    words = re.findall(r'\b[a-z0-9]+\b', text)
    unique = sorted(set(words))
    return unique

def collapse_duplicates(text, char):
    result = []
    prev = ""
    
    for c in text:
        if c == char and prev == char:
            continue
        result.append(c)
        prev = c
    
    return ''.join(result)

