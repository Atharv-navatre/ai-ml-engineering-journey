'''
Q4. Given a tuple of integers, create:
• A tuple of all even numbers
• A tuple of all odd numbers

'''


tup = (1, 2, 3, 4, 5, 6)

even = []
odd = []

for num in tup:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

even_tuple = tuple(even)
odd_tuple = tuple(odd)

print("Even:", even_tuple)
print("Odd:", odd_tuple)