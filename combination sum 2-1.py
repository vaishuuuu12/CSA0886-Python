candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8
candidates.sort()
result = []
combination = []
def backtrack(start, target):
    if target == 0:
        result.append(combination[:])
        return
    if target < 0:
        return
    for i in range(start, len(candidates)):
        if i > start and candidates[i] == candidates[i - 1]:
            continue
        combination.append(candidates[i])
        backtrack(i + 1, target - candidates[i])
        combination.pop()
backtrack(0, target)
print(result)
