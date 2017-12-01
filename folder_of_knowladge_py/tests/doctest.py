def skip(f):
    return None
def lol(sth):
    """
    >>> lol('hello')
    'HELLO!'
    >>> lol('lmao')
    'LMAO!'
    """
    #sth=sth.upper()
    #sth.append('!')
    #return sth

if __name__ == '__main__':
    import doctest
    doctest.testmod()
