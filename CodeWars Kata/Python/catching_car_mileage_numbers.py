def is_palindrome(number, awesome_phrases):
    return str(number) == str(number)[::-1]

def is_seq_inc(number, awesome_phrases):
    return str(number) in '1234567890'

def is_seq_dec(number, awesome_phrases):
    return str(number) in '9876543210'

def is_same_digit(num, awesome_phrases):
    return str(num) == str(num)[0] * len(str(num))

def is_zeros(num, awesome_phrases):
    return str(num)[1:] == (len(str(num)) - 1) * '0'

def is_awesome(num, awesome_phrases):
    for number in awesome_phrases:
        if number == num:
            return True
    return False


def is_interesting(number, awesome_phrases):
    tests = [is_palindrome,is_awesome,is_zeros,is_same_digit,is_seq_inc,is_seq_dec]
    
    for _ in range(3):
        current = number + _
        if current > 99 and any([test(current, awesome_phrases) for test in tests]):
            return 2 if _ == 0 else 1
        
    return 0
