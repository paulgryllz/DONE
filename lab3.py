def is_long(str):
    '''(str) -> str
    Return if a string is very long or kinda short
    >>> is_long('Hello')
    'kinda short'
    >>> is_long('It is partly cloudy outside')
    'Very long'
    '''
    if (len(str) >= 10):
        return 'Very long'
    elif (len(str) <= 10):
        return 'kinda short'
def longer(str1, str2):
    '''(str) -> str
    Return the length of the longer string given two strings
    >>> longer('Hello', 'Greetings')
    '9'
    >>> longer('Bye', 'Goodbye')
    '7'
    '''
    if (len(str1) > len(str2)):
        return len(str1)
    elif (len(str1) < len(str2)):
        return len(str2)
def earlier(str1, str2):
    '''(str) -> str
    Return the string that would appear earlier in the dictionary
    >>> earlier('Cat', 'Dog')
    'Cat'
    >>> earlier('World', 'Hello')
    'Hello'
    '''
    if str1 < str2:
        return str1
    elif str1 > str2:
        return str2
def where(str1, str2):
    '''(str) -> str
    Return the first occurrence of the second string in the first string
    >>> where('lol', 'l')
    '0'
    >>> where('Ahmer', 'h')
    '1'
    '''
    return str1.find(str2)
def is_vowel(str):
    '''(str) -> str
    Return True if the one character string is a vowel, otherwise return False
    >>> is_vowel('o')
    'True'
    >>> is_vowel('l')
    'False'
    '''
    if str in 'aeiou':
        return 'True'
    else:
        return 'False'
def count_letter(str1, str2):
    '''(str) -> str
    Return all occurrences of the second string in the first and return count
    >>> count_letter('Banana', 'a')
    '3'
    >>> count_letter('Tricycle', 'c')
    '2'
    '''
    return str1.count(str2)
def remove_digits(str):
    '''(str) -> str
    Return the original string but with the digits removed
    >>> remove_digits('thirty30')
    'thirty'
    >>> remove_digits('fiftynine50')
    'fiftynine'
    '''
    ret = ''
    for i in str:
        if i.isalpha():
            ret += i
    return ret
def repeat_character(str1, str2):
    '''(str) -> str
    Return the repeat the 2nd string as many times as it occurs in string1
    >>> repeat_character('Hello', 'l')
    'll'
    >>> repeat_character('Apple', 'p')
    'pp'
    '''
    return str2 * str1.count(str2)