arr = [6, 7, 8, 9, 1, 2, 3, 4, 5]
target = 3
start = 0
end = len(arr) - 1
while start <= end:
    mid = (start + end) // 2
    if arr[mid] == target:
        print(f"Element {target} found at index {mid}")
        break
    if arr[start] <= arr[mid]:  
        if arr[start] <= target < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    else: 
        if arr[mid] < target <= arr[end]:
            else: 
            end = mid - 1
else:
    print(f"Element {target} not found in the array")
