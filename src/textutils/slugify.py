import re

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
