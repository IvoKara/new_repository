import time
import random
import sys

a=[]
for item in range(10000):
    a.append(random.randint(0, 1000000000000))
print("list {}b".format(sys.getsizeof(a)))
t1 = time.clock()
for num in a:
    pass
t2 = time.clock()
print("time: {}ms".format( t2-t1))

a=iter(a)
print("iterator {}b".format(sys.getsizeof(a)))
t1 = time.clock()
for num in a:
    pass
t2 = time.clock()
print("time: {}ms".format( t2-t1))

a = (i for i in a)
print("generator {}b".format(sys.getsizeof(a)))
t3 = time.clock()
for num in a:
    pass
t4 = time.clock()
print("time: {}ms".format( t4-t3))
