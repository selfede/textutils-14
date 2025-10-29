import re
import string

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


def word_lengths(text):
    words = text.split()
    
    result = {}
    
    for word in words:
        length = len(word)
        result[word] = length
    
    return result

def average_word_length(text: str) -> float:

    if not text:
        return 0.0

    words = re.findall(r"[a-zA-Z0-9]+", text)

    if not words:
        return 0.0
    
    total_length = sum(len(word) for word in words)
    avg_length = total_length / len(words)
    return round(avg_length, 2)

def remove_punctuation(text):
    cleaned_text = ""
    for ch in text:
        if ch not in string.punctuation:
            cleaned_text += ch

    return cleaned_text