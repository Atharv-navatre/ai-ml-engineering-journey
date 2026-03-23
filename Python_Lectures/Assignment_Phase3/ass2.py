# Q2. Given a list of integers compute the average of all numbers in the list.

nums = [10, 20, 30, 40]

total = 0

for n in nums:
    total += n

average = total / len(nums)

print("Average:", average)