def find_first_differing_letter_index(left, right):
    for index, left_letter in enumerate(left):
        if left_letter != right[index]:
            return index


def is_substitution(left, right):
    differing_index = find_first_differing_letter_index(left, right)
    if ((left[:differing_index] == right[:differing_index]) and
        (left[differing_index + 1:] == right[differing_index + 1:])):
        return True
    return False


def is_addition(left, right):
    differing_index = find_first_differing_letter_index(left, right)
    if differing_index is None:
        return True
    if ((left[:differing_index] == right[:differing_index]) and
        (left[differing_index:]) == right[differing_index + 1:]):
        return True
    return False


def is_substraction(left, right):
    if right in left:
        return True
    differing_index = find_first_differing_letter_index(left, right)
    if ((left[:differing_index] == right[:differing_index]) and
        (left[differing_index + 1:]) == right[differing_index:]):
        return True
    return False
