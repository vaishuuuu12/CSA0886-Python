import itertools
elements = [1, 2, 2]
subsets = [list(subset) for i in range(len(elements) + 1) for subset in itertools.combinations(elements, i)]

print(subsets)
