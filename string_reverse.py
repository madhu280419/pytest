def reversestring(s):
    return s[::-1]

def test_reversestring():
    assert reversestring("Madhu") == "uhdaM"
    assert reversestring("madhu") != "yala"