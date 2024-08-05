arr = [1, 1, 2, 3, 3, 4, 5, 5, 6]
unique_index = 0
for i in range(1, len(arr)):
    if arr[i] = arr[unique_index]:
        unique_index += 1
        arr[unique_index] = arr[i]
        new_length = unique_index + 1
        arr = arr[:new_length]
print(arr)
