import next_palindrome as p

def test_242_is_palindrome():
    assert p.is_palindrome(242) == True

def test_243_is_not_a_palindrome():
    assert p.is_palindrome(243) == False
     
def test_2442_is_palindrome():
    assert p.is_palindrome(2442) == True

def test_number_under_10():
    assert p.is_palindrome(5) == True

def test_negative_number():
    assert p.is_palindrome(-55) == True

def test_next_palindrome_for_492_is_494():
    assert p.next_palindrome(492) == 494