def is_even(n):
    return n % 2 == 0

def test_is_even():
    assert is_even(4)
    assert not is_even(9)
