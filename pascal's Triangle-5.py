def get_row(rowIndex):
    row = [1]
    for _ in range(rowIndex):
        row = [x + y for x, y in zip([0] + row, row + [0])]
    
    return row
rowIndex = 3
print(get_row(rowIndex))  
