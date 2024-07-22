def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num
    return result
nums1 = [2, 2, 1]
print(f"The single number in {nums1} is: {singleNumber(nums1)}")

