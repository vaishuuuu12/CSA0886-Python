def searchInsert(nums, target):
    left, right = 0, nums.length - 1
    
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return left
nums = [1, 3, 5, 6]
target = 5
index = searchInsert(nums, target)
print(f"Index of target {target} is: {index}")
