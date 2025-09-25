from twttr import shorten
def test_shorten_by_lower():
    assert shorten("twitter") == "twttr"

def test_shorten_upper():
    assert shorten('EmzEdam') == 'mzdm'
