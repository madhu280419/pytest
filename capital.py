
def capitalize_text(s):
    return s.title()

def test_capitalize_text():
    assert capitalize_text("hello world") == "Hello World"
    assert capitalize_text("python testing") == "Python Testing"
