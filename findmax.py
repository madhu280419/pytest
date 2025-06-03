def find_max(lst):
    return max(lst)

def test_find_max():
    assert find_max([1, 3, 6, 4, 9, 5, 7]) == 9

def test_find_max_not_equal():
    assert find_max([1, 7, 3, 6, 5]) != 6  
    