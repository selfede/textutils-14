def collapse_duplicates(text, char):
    result = []
    prev = ""
    
    for c in text:
        if c == char and prev == char:
            continue
        result.append(c)
        prev = c
    
    return ''.join(result)