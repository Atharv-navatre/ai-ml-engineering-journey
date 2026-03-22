'''
Let’s create a Simple that performs arithmetic operations. Create
a function that performs addition, subtraction,
multiplication, or division based on the parameter.
Q8 Calculator
calculator(a, b, operation)
operation
[ operation parameter can have values ‘+’ , ‘-’ , '*’ & ‘/’ .

'''

def calculator(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        if b != 0:
            return a / b
        else:
            return "Division by zero not allowed"
    else:
        return "Invalid operation"

# taking input
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operation (+, -, *, /): ")

result = calculator(a, b, op)
print("Result:", result)