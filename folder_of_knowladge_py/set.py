sample = {'a', 'e', 'a', 'a', 'i', 'o', 'u', 'u'}
print(sample == {'a','e','i','o','u'})
#sample[1] = 6
sample.add('y')                     #faster to check whether
print(sample)                       #an item is part of a set,
                                    #rather than part of a list.
first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}
print(first.union(second))
print(first.union(second) == second.union(first) == first | second)
print(first & second)   #intersection
print(first ^ second)   #symmtric_difference
print(first, second)
print(first - second)   #difference
print(second - first)   #{7,8,9} are in second but not in first
