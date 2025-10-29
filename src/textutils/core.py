import re

def average_word_length(text: str) -> float:

    if not text:
        return 0.0

    words = re.findall(r"[a-zA-Z0-9]+", text)

    if not words:
        return 0.0
    
    total_length = sum(len(word) for word in words)
    avg_length = total_length / len(words)
    return round(avg_length, 2)