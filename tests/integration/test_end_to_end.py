import textutils.core as c

def test_complete_text_processing_pipeline_1():
    """Test full pipeline: blog post title processing"""
    # Starting with messy blog title
    text = "Python!!!   Tips & Tricks...For   Beginners???"
    
    #Remove punctuation
    cleaned = c.remove_punctuation(text)
    assert cleaned == "Python   Tips  TricksFor   Beginners"
    
    #Collapse duplicate spaces
    normalized = c.collapse_duplicates(cleaned, ' ')
    assert normalized == "Python Tips TricksFor Beginners"
    
    #Count vowels
    vowels = c.count_vowels(normalized)
    assert vowels == 7
    
    #Get unique words
    unique = c.unique_words(normalized)
    assert unique == ["beginners", "python", "tips", "tricksfor"]
    
    #Get word lengths
    lengths = c.word_lengths(normalized)
    assert lengths == {"Python": 6, "Tips": 4, "TricksFor": 9, "Beginners": 9}
    
    #Calculate average word length
    avg = c.average_word_length(normalized)
    assert avg == 7.0
    
    #Create URL slug
    slug = c.slugify(cleaned)
    assert slug == "python-tips-tricksfor-beginners"