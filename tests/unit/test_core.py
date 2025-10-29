import textutils.core as c

def test_slugify_basic():
    
    text = "Hello World"
    assert c.slugify(text) == "hello-world"

def test_slugify_removes_special_characters():
    
    text = "Fast & Furious: Tokyo Drift!"
    assert c.slugify(text) == "fast-furious-tokyo-drift"