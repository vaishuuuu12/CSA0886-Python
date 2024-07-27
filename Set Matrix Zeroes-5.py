def set_zeroes(matrix):
    m, n = len(matrix), len(matrix[0])
    first_row_has_zero = any(matrix[0][j] == 0 for j in range(n))
    first_col_has_zero = any(matrix[i][0] == 0 for i in range(m))
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = matrix[0][j] = 0
    for i in range(1, m):
        if matrix[i][0] == 0:
            for j in range(1, n):
                matrix[i][j] = 0

    for j in range(1, n):
        if matrix[0][j] == 0:
            for i in range(1, m):
                matrix[i][j] = 0
    if first_row_has_zero:
        for j in range(n):
            matrix[0][j] = 0

    if first_col_has_zero:
        for i in range(m):
            matrix[i][0] = 0
matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
set_zeroes(matrix)
print(matrix)  
