def palindrome(s):
    return s == s[::-1]


def test_palindrome_true():
    assert palindrome("tenet")
    
def test_palindrome_false():
    assert not palindrome("madhu")
    
def test_palindrome_empty_true():
    assert palindrome("")

def test_palindrome_single_char_true():
    assert palindrome("a")
