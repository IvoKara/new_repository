from collections import deque

#fast inserting and removing list

def doodledPassword(digits):
    n = len(digits)
    res = [deque(digits) for _ in range(n)]
    deque(map(lambda d: res[d].rotate(-d), range(n)), 0)
    return [list(d) for d in res]
