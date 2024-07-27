nums = [1, -2, 3, 4, -1, 2, 1, -5, 4]
max_current = max_global = nums[0]
for num in nums[1:]:
    max_current = max(num, max_current + num)
    if max_current > max_global:
        max_global = max_current
print(max_global)
