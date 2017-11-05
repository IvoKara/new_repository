'''def a(x):     #stack overflow
    print('a')
    x(a)

a(a)'''
from functools import reduce

a=[5,7,8,11,20]
l=list(filter(lambda x: x%2,a))
print(l)

b=[12,7,22,19,69]
map1=list(map(lambda y:y*2,b))
print(map1)

s="helloooolmao"
map2=list(map(lambda x: x.upper(),s))
print(map2)

print("ASCII code",ord("a"))
print("reverse", chr(97))

la=lambda c: chr(ord(c)+(ord("A")-ord("a")))
map3=list(map(la,s))
print(map3)

#search for reduce

r = [1,4,55,-87,69,0]
red=reduce(lambda x,y: x+y,r)
print(red)
