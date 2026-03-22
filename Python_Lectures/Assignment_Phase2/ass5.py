'''
Q5. Write a function to return the sum of digits of a number, n .
'''

def sum_of_digits(n):
    total = 0

    while n > 0:
        digit = n % 10
        total += digit
        n = n // 10

    return total

num = int(input("Enter num: "))
print("Total sum:", sum_of_digits(num))









