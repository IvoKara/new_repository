l = list(zip([1,2,3,4], [5,6,7,8]))
print(l)
print(list(zip(*l)))  # * means that all tuples are presented as separate arguments
#Output:
#>>> [(1,2,3,4), (5,6,7,8)] 
