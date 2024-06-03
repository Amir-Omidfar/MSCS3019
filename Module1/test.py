from collections import Counter
words = ["apple","apple","orange","melon"] 
nums = [1,1,1,2,3,4,5,5]
counts = Counter(nums)
print(counts[1])
for num in counts:
    print(counts[num])
    