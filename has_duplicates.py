lst = [1, 2, 3, 4, 5, 3]
has_duplicates = False
seen = set()
for item in lst:
    if item in seen:
        has_duplicates = True
        break
    seen.add(item)
print(has_duplicates)
