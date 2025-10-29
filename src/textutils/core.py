import string

def remove_punctuation(text):
    cleaned_text = ""
    for ch in text:
        if ch not in string.punctuation:
            cleaned_text += ch

    return cleaned_text