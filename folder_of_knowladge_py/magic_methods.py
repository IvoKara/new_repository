class Sum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __add__(s, oth):
        return Sum(s.a+oth.a,s.b+oth.b)
    def __mul__(s,oth): 
        return Sum(s.a*oth.a,s.b*oth.b)

class Comp:
    def __init__(self, a):
        self.a = a
    def __ge__(s, oth):
        return s.a >= oth.a
    def __ne__(s, oth):
        return s.a != oth.a

class List:
    def __init__(self, a):
        self.a = a
    def __len__(self):
        return len(self.a)
    def __getitem__(self, index):
        return self.a[index]
    def __setitem__(self,index,value):
        self.a[index] = value
        return self.a[index]
    def __contains__(self, value):
        return value in self.a
    def __iter__(self):
        self.a = iter(self.a)
        self.i = -1
        return self.a
    def __next__(self):
        self.i += 1
        if slef.i != len(self.a) - 1:
            return self.a[slef.i]
        else:
            raise StopIteration
        next()
one = Sum(4,6)
two = Sum(5,1)
res = one + two
print(res.a,res.b)
res = one * two
print(res.a,res.b)

one = Comp(0)
two = Comp(-4)
print(two>=one)
print(two!=one)

one = List([1,2,3,4])
print(len(one))
print(one[1])
one[1] = 5
print(one[1])
print(2 in one)
for i in one:
    print(i)
