nums = [2, 3, 1, 1, 4]
n = len(nums)
if n <= 1:
    print(0)
else:
    jumps = 0
    current_end = 0
    farthest = 0

    for i in range(n - 1):
        farthest = max(farthest, i + nums[i])
        if i == current_end:
            jumps += 1
            current_end = farthest
            if current_end >= n - 1:
                break
    print(jumps)
