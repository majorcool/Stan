from itertools import permutations
def perms(l):
    a=list(permutations(l,5))
    return a
print(perms([1,2,3,4,5]))
print(len(perms([1,2,3,4,5])),"items in list")