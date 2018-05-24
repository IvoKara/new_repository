from itertools import permutations

def rockPaperScissors(players):  #who with who will battle
    return sorted(permutations(players,2))

def kthPermutation(numbers, k):  #all possible combinations of numbers
    return list(permutations(numbers))[k-1]
