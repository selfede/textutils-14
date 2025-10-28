def word_lengths(text):
    words = text.split()
    
    result = {}
    
    for word in words:
        length = len(word)
        result[word] = length
    
    return result