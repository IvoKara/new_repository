def groupDating(male, female):
    return [[l[x] for x in range(len(male)) if male[x]!=female[x]] for l in (male,female)]

#del if male[x]==female[x]
