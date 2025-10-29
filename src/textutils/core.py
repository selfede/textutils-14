import re
<<<<<<< HEAD
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


def count_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for char in text:
        if char.lower() in vowels:
            count += 1
    return count
=======

def slugify(text):
    text = text.lower()
    text = text.replace(' ', '-')

    result = ''
    for char in text:
        if char.isalnum() or char == '-':
            result += char

    result = re.sub(r'-+', '-', result)
    result = result.strip('-')

    return result
>>>>>>> florian-collaborative-branch
