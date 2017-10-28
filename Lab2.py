import doctest

def windchill_category(wc):
    ''' (number) -> str
    Return the windchill given a temperature
    >>> windchill_category(-3)
    'low'
    >>> windchill_category(-12)
    'moderate'
    >>> windchill_category(-39)
    'Cold'
    >>> windchill_category(-90)
    'Extreme'
    '''
    if (-9 <= wc) and (wc <= 0):
        return 'low'
    elif (-24 <= wc) and (wc <= -10):
        return 'moderate'
    elif (-44 <= wc) and (wc <= -25):
        return 'Cold'
    elif (wc == -45) or (-45 > wc):
        return 'Extreme'  
if __name__ == '__main__':
    doctest.testmod(verbose=True)