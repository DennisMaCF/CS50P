from twttr import shorten

#
def test_shorten():
    assert shorten("aeiou") == ""
    assert shorten("AEIOU") == ""
    assert shorten("twitter") == "twttr"
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("1a2be") == "12b"
    assert shorten("What's your name?") == "Wht's yr nm?"
