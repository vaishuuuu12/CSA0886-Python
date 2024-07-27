import itertools
nums = [1, 2, 3]
permutations = list(itertools.permutations(nums))
permutations = [list(perm) for perm in permutations]
print(permutations)
