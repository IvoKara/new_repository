import itertools as it
for i in it.count(3):   #ifinete from 3
    print(i)
    if i == 10:
        break

some_str = "Here is nothing interesting"
for i in it.cycle(some_str): #infinite iteration
    print(i)
    if i == "g":
        break
nums = list(it.accumulate(range(8))) #reduce
print(nums)
print(list(it.takewhile(lambda x: x<= 6, nums)))#map

print(list(it.permutations(["a","b","c"])))
print(list(it.product(["a","b"],["c", "d"])))
