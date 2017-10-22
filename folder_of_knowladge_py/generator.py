import sys
import random
import time

names = ["John", "Coreny", "Adam","Steve","Rick","Thomas"]
majors = ["Math" ,"Engineering", "CompSci", "Arts", "Bussines"]

def ppl_l(n):
    res=[]
    for i in range(n):
        person ={
                    "id": i,
                    "name": random.choice(names),
                    "major": random.choice(majors)
                }
        res.append(person)
    return res

def ppl_g(n):
    res=[]
    for i in range(n):
        person ={
                    "id": i,
                    "name": random.choice(names),
                    "major": random.choice(majors)
                }
        yield person

print("Memory list(Before): {}b".format(sys.getsizeof(ppl_l(1000000))))
print("Memory generator(Before): {}b".format(sys.getsizeof(ppl_g(1000000))))
