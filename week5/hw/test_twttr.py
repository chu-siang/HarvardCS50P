from twttr import shorten


def test_str():
    assert shorten("CS50") == "CS50"
    assert shorten("Twitter") == "Twttr" 
    assert shorten("What's your name?") == "Wht's yr nm?"
    assert shorten("PYTHON") == "PYTHN"