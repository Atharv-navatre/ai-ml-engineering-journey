# Swap two numbers using a temporary variable

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

temp = a
a = b
b = temp

print("After swapping:")
print("a =", a)
print("b =", b)


'''
# Swap two numbers using Python shortcut

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

a, b = b, a

print("After swapping:")
print("a =", a)
print("b =", b)
'''