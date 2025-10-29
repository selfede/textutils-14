import textutils.core as collpase

def test_basic_collapse():
    # covers duplicate skipping (True branch)
    assert collpase.collapse_duplicates("heeellooo", "e") == "hellooo"

def test_no_duplicates():
    # covers normal flow (False branch)
    assert collpase.collapse_duplicates("hello", "x") == "hello"

def test_empty_string():
    # covers edge case: empty input
    assert collpase.collapse_duplicates("", "a") == ""
