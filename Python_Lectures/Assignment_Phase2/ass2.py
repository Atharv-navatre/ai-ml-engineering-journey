'''
Write a function that takes two integers and and prints all even
numbers between them (inclusive).

'''

def print_even_numbers(a, b):
    for num in range(a, b + 1):
        if num % 2 == 0:
            print(num)

# taking input
start = int(input("Enter first number: "))
end = int(input("Enter second number: "))

print_even_numbers(start, end)