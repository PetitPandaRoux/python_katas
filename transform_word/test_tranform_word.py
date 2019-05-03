import transform_word as tw


def test_differing_index_three_letters():
    assert tw.find_first_differing_letter_index('cat', 'cut') == 1


def test_differing_index_four_letters():
    assert tw.find_first_differing_letter_index('abcd', 'bbcd') == 0


def test_differing_index_multiple_occurences():
    assert tw.find_first_differing_letter_index('abbcd', 'abccd') == 2


def test_is_not_subsitution():
    assert tw.is_substitution('abc', 'bac') == False


def test_is_substitution():
    assert tw.is_substitution('crave', 'crate') == True


def test_is_substitution_2():
    assert tw.is_substitution('abc', 'bbc') == True


def test_is_substitution_3():
    assert tw.is_substitution('abc', 'abd') == True


def test_is_not_addition():
    assert tw.is_addition('abcd', 'abbbbb') == False


def test_is_addition():
    assert tw.is_addition('abcd', 'abzcd') == True


def test_is_addition_2():
    assert tw.is_addition('abcd', 'aabcd') == True


def test_is_addition_3():
    assert tw.is_addition('abc', 'abcd') == True


def test_is_not_substraction():
    assert tw.is_substraction('abcd', 'abb') == False


def test_is_substraction():
    assert tw.is_substraction('abcd', 'abd') == True


def test_is_substraction_2():
    assert tw.is_substraction('abcd', 'bcd') == True


def test_is_substraction_3():
    assert tw.is_substraction('abcd', 'abc') == True
