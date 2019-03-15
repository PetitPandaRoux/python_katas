def is_palindrome(number):
    number_string = str(abs(number))
    if number_string[::-1] == number_string:
        return True
    else:
        return False