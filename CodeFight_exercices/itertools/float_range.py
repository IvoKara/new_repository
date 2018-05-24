from itertools import takewhile, count

def floatRange(start, stop, step):
    gen = takewhile(lambda x: x<stop, count(start,step))
    return list(map(lambda x: round(x, 5),gen))
