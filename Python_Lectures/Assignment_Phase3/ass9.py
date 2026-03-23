# Q9. Given a list, print all elements that appear more than once in the list.
# [Hint - use sets]


nums = [1, 2, 3, 3, 4, 5]

seen = set()
duplicates = set()

for num in nums:
    if num in seen:
        duplicates.add(num)
    else:
        seen.add(num)

print("Duplicate elements:", duplicates)