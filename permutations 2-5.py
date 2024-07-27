import itertools
nums = [1, 1, 2]
permutations = list(itertools.permutations(nums))
unique_permutations = set(permutations)
unique_permutations = [list(perm) for perm in unique_permutations]
print(unique_permutations)
