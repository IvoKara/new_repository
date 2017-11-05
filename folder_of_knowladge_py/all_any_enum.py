nums = [55, 44, 33, 22, 11]

if all([elem>5 for elem in nums]):        #if all elem are bigger
    print("all are bigger than 5")        # than 5 (all are true) 1 and 2 and 3...
    
if any([elem %2== 0 for elem in nums]):
    print("at least one is even")

for v in enumerate(nums):
    print(v)

print(list(enumerate(nums)))
