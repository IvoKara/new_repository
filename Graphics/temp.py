def maxes(l):
    copy = l.copy()
    m = max(l)
    ind=[]
    for  i in range(copy.count(m)):
        ind.append(copy.index(m)+i)
        copy.pop(copy.index(m))
    return ind
                    
##n = int(input().strip())
##a = input().strip().split(" ")
##a = list(map(int,a))
a = [1,2,5,2,6,5,6,3,1,2,0,1]
ind= maxes(a)
for i in range(len(a)):
    if i>=ind[0] and i<=ind[len(ind)-1]:
        a[i]=max(a)
print(a)
