nums = [2, 3, 1, 1, 4]  
max_reachable = 0
for i in range(len(nums)):
    if i > max_reachable:
        print(False)
        break
    max_reachable = max(max_reachable, i + nums[i])
    if max_reachable >= len(nums) - 1:
        print(True)
        break
