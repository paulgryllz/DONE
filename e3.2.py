import doctest


def remove_punctuation(s):
    '''(str) -> str
    Return s with all non-space or non-alphanumeric
    characters removed.
    >>> remove_punctuation('a, b, c, 3!!')
    'a b c 3'
    '''
    # first we create a empty string for appending sanitized characters
    ret = ""
    # we loop through the input string checking if it's ascii value is in our
    # acceptable range
    for i in s:
        asc_char = ord(i)
        if asc_char in range(65, 91) or asc_char in range(97, 123) or\
           asc_char in range(48, 58) or asc_char == 32:
            # if the character is alphanumeric or a space we append to our
            # return string
            ret += i
    return ret


def separate(mixed):
    '''(str) -> str
    Mixed has only letters and numbers in it.  Return a
    new string that has the letters from mixed in the same order
    they appear in mixed followed by the numbers in mixed in the
    same order they appear in mixed.
    >>> separate('a8c9b60x10')
    'acbx896010'
    '''
    num_str = ""
    alpha_list = ""
    for i in mixed:
        asc_char = ord(i)
        if asc_char in range(65, 91) or asc_char in range(97, 123):
            alpha_list += i
        elif asc_char in range(48, 58):
            num_str += i
    return alpha_list + num_str


def encrypt(msg, code):
    '''(str, str) -> str
    Return msg encrypted using the given code.  The code
    is an ordering of the alphabet plus the space and '.'
    characters. The position of each character in the code
    string gives the index of the replacement character in
    the regular alphabet 'abcdefghijklmnopqrstuvwxyz .'

    In the first example below, 'h' is in position 20, so we
    select the letter in position 20 in the alphabet, or 'u'.

    >>> encrypt('hello there', '. zyxwvutsrqponmlkjihgfedcba')
    'uxqqnbiuxkx'
    >>> encrypt('hello there', '. zaybxcwdveuftgshriqjpkolnm')
    'rlzzyborlsl'
    '''
    regular_alpha = 'abcdefghijklmnopqrstuvwxyz .'
    ret = ""
    for i in msg:
        curr = code.find(i)
        ret += regular_alpha[curr]
    return ret


if __name__ == '__main__':
    doctest.testmod(verbose=True)
