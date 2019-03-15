from roman_to_number import roman_to_number

def test_I_give_1():
    assert roman_to_number('I') == 1

def test_V_give_1():
    assert roman_to_number('V') == 5

def test_C_give_100():
    assert roman_to_number('C') == 100

def test_D_give_500():
    assert roman_to_number('D') == 500

def test_II_give_2():
    assert roman_to_number('II') == 2

def test_VI_give_6():
    assert roman_to_number('VI') == 6

def test_IV_give_4():
    assert roman_to_number('IV') == 4

def test_IV_give_9():
    assert roman_to_number('IX') == 9

def test_XIX_give_19():
    assert roman_to_number('XIX') == 19

def test_XL_give_40():
    assert roman_to_number('XL') == 40

def test_XCIX_give_99():
    assert roman_to_number('XCIX') == 99

def test_CD_give_400():
    assert roman_to_number('CD') == 400

def test_CM_give_99():
    assert roman_to_number('CM') == 900

def test_MMMMCMXCIX_give_4999():
    assert roman_to_number('MMMMCMXCIX') == 4999