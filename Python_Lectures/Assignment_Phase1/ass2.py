# Take two numbers as input and print sum, difference, product and quotient

a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))

addition = a + b
difference = a - b
product = a * b

if b != 0:
    quotient = a / b
else:
    quotient = "Undefined (division by zero)"

print("Sum:", addition)
print("Difference:", difference)
print("Product:", product)
print("Quotient:", quotient)