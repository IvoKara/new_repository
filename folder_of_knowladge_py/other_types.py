import time
sample = [["Ivo", 16], ["Alex", 7]]

print()
sample = dict(sample)
sample["Elena"] = 39
print(sample)
print("Ivo" in sample)
print(sample.get("Jordan", "not in the dict"))
print(sample.get("Ivo")==sample["Ivo"])
print(sample.items())
##bad_dict = {
##  [1, 2, 3]: "one two three", 
##}

print()
print(tuple(sample))
sample = ("Alex", 10),("Ivo", 16)
print(sample)

print()
print(set(sample))
lol = range(10)
lol = lol[::-1]
print(lol)

sample = list(range(1001))
t1=time.clock()
for x in sample:
    pass
t2=time.clock()
print("list ",t2-t1)

t1=time.clock()
for x in tuple(sample):
    pass
t2=time.clock()
print("tuple",t2-t1)
