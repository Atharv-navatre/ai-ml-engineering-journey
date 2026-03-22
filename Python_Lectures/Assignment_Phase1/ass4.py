# User enters a string containing a number

num_str = input("Enter a number: ")

# Convert to integer
num_int = int(num_str)

# Convert to float
num_float = float(num_str)

# Convert back to string
num_string = str(num_int)

# Print values with their types
print("Integer:", num_int, "Type:", type(num_int))
print("Float:", num_float, "Type:", type(num_float))
print("String:", num_string, "Type:", type(num_string))