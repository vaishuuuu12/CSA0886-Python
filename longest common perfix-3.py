import os
def longest_common_prefix(strings):
    return os.path.commonprefix(strings)
print(longest_common_prefix(["flower","flow","flight"]))
