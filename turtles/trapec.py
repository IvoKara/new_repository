import math

a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

d = math.fabs(a - b)/2
    
if d<c:
    h = math.sqrt(c**2 - d**2)
    S = ((a + b)/2)*h
    print(int(S))
else:
    print('Некоректни данни')
