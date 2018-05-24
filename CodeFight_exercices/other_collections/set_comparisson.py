def correctScholarships(bestStudents, scholarships, allStudents):
    return set(bestStudents) <= set(scholarships) < set(allStudents)

#like an ordinary ints
#A < B less i.e. B contains all elements in A
#A <= B less or equal i.e. like above BUT A can be equal to B
