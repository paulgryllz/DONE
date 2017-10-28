# do not remove this import statement

import doctest

# do not change the docstrings - we will use these examples
# to test your functions using doctest.

def storm_category(speed):
    '''(int) -> int 
    Return the category the wind speed belongs to.
    >>> storm_category(90)
    0
    >>> storm_category(130)
    1
    >>> storm_category(165)
    2
    >>> storm_category(190)
    3
    >>> storm_category(220)
    4
    >>> storm_category(260)
    5
    '''
    if (0 <= speed <= 118):
        return 0
    elif (119 <= speed <= 153):
        return 1
    elif (154 <= speed <= 177):
        return 2
    elif (178 <= speed <= 208):
        return 3
    elif (209 <= speed <= 251):
        return 4
    elif (252 == speed) or (252 < speed):
        return 5

def category_warning(category):
    '''(int) -> str 
    Return a warning message for the storm associated 
    with the given storm category.  
    
    Requirement: 0 <= category <= 5
	
    >>> category_warning(0)
    'Not a major threat.'
    >>> category_warning(1)
    'Very dangerous winds will produce some damage.'
    >>> category_warning(2)
    'Extremely dangerous winds will cause extensive damage.'
    >>> category_warning(3)
    'Devastating damage will occur.'
    >>> category_warning(4)
    'Catastrophic damage will occur.'
    >>> category_warning(5)
    'Cataclysmic damage will occur.'
    '''
    if (0 == category):
        return 'Not a major threat.'
    elif (1 == category):
        return 'Very dangerous winds will produce some damage.'
    elif (2 == category):
        return 'Extremely dangerous winds will cause extensive damage.'
    elif (3 == category):
        return 'Devastating damage will occur.'
    elif (4 == category):
        return 'Catastrophic damage will occur.'
    elif (5 == category):
        return 'Cataclysmic damage will occur.'
    
def warning(speed):
    '''(int) -> str
    Given a storm wind speed, return the associated warning 
    message.
    >>> warning(90)
    'Not a major threat.'
    >>> warning(130)
    'Very dangerous winds will produce some damage.'
    >>> warning(165)
    'Extremely dangerous winds will cause extensive damage.'
    >>> warning(199)
    'Devastating damage will occur.'
    >>> warning(225)
    'Catastrophic damage will occur.'
    >>> warning(280)
    'Cataclysmic damage will occur.'
    '''    
    # Requirement: this function should be one line!
    return category_warning(storm_category(speed))
    
# do not remove this if __name__ == '__main__': statement

if __name__ == '__main__':
    
    # After you have finished writing your functions
    # remove the comment symbol and remove
    # the line "pass" and run your file.
    # this will output whether your functions pass the 
    # docstring examples
    
    doctest.testmod(verbose=True)
    