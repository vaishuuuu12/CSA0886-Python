from collections import defaultdict
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
anagrams = defaultdict(list)
for word in strs:
    sorted_word = ''.join(sorted(word))
    anagrams[sorted_word].append(word)
result = list(anagrams.values())
print(result)
