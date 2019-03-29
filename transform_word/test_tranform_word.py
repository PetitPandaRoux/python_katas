import transform_word as tw


# def test_trajet():
#     resultat = ['abcde', 'abcd', 'abc', 'abz', 'ayz', 'xyz']
#     assert tw.trajet('abcde', 'xyz') == resultat

def test_reduit_de_1():
    assert tw.reduit('abcde') == 'abcd'


def test_reduit_de_1_bis():
    assert tw.reduit('abcd') == 'abc'


def test_reduit_jusque_cible():
    trajet_vers_cible = ['abcd', 'abc']
    assert tw.transforme_longueur('abcde', 'abc') == trajet_vers_cible


def test_augmente_de_1():
    assert tw.augmente('abc','d') == 'abcd'


def test_augmente_de_1_bis():
    assert tw.augmente('abc','z') == 'abcz'


def test_augmente_jusque_cible():
    trajet_vers_cible = ['abcx','abcxy', 'abcxyz']
    assert tw.transforme_longueur('abc','abcxyz') == trajet_vers_cible
