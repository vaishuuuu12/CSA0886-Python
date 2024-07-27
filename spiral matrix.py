matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = []
top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1

while top <= bottom and left <= right:
    result.extend(matrix[top][left:right+1])  # Traverse from left to right
    top += 1
    result.extend(row[right] for row in matrix[top:bottom+1])  # Traverse from top to bottom
    right -= 1
    if top <= bottom:
        result.extend(matrix[bottom][left:right+1][::-1])  # Traverse from right to left
        bottom -= 1
    if left <= right:
        result.extend(row[left] for row in matrix[top:bottom+1][::-1])  # Traverse from bottom to top
        left += 1

print(result)
