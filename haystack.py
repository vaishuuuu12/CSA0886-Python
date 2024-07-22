def strStr(haystack, needle):
    return haystack.find(needle)

# Example usage:
haystack = "sadbutsad"
needle = "sad"
index = strStr(haystack, needle)
print(f"The index of the first occurrence of '{needle}' in '{haystack}' is: {index}")
