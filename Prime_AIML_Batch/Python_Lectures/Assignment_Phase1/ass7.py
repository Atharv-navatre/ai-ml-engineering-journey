# Ask the user for temperature in Celsius (string input)

celsius_str = input("Enter temperature in Celsius: ")

# Convert string to float
celsius = float(celsius_str)

# Convert Celsius to Fahrenheit
fahrenheit = (celsius * (9/5)) + 32

# Print result
print("Temperature in Fahrenheit:", fahrenheit)