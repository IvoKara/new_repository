#element that only appear once
def singleNumber(nums):
    res = 0
    for num in nums:
        res ^= num
    return res


#swaps first with second, third with forth...
def correctLineup(athletes):
    return [athletes[x^1] for x in range(len(athletes))]

# 1^0=1
# 1^1=0
# 1^2=3
# 1^3=2
