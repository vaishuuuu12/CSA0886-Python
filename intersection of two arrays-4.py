def intersection(nums1: list[int], nums2: list[int]) -> list[int]:
    set1 = set(nums1)
    set2 = set(nums2)
    return list(set1 & set2)
print(intersection([1, 2, 2, 1], [2, 2]))
