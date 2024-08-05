list_of_lists = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
total_sum = 0
for sublist in list_of_lists:
    for number in sublist:
        total_sum += number
print(total_sum)
