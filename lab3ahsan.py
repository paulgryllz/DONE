def is_long(srz):
    return 'very long' if (len(srz) > 10) else 'kinda short'


def longer(str1, str2):
    if len(str1) > len(str2):
        return len(str1)
    else:
        return len(str2)


def earlier(str1, str2):
    if str1 < str2:
        return str1
    else:
        return str2


def where(str1, str2):
    return str1.find(str2)


def is_vowel(str1):
    return True if str1 in 'aeiou' else False


def count_letter(str1, str2):
    return str1.count(str2)


def remove_digits(str1):
    ret = ''
    for i in str1:
        if i.isalpha():
            ret += i
    return ret
