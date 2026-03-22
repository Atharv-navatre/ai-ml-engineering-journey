# Program to check positive or negative until user enters "Quit"

while True:
    user_input = input("Enter a number (or type 'Quit' to exit): ")

    if user_input.lower() == "quit":
        print("Program ended.")
        break

    n = float(user_input)

    if n > 0:
        print("Positive number")
    elif n < 0:
        print("Negative number")
    else:
        print("Zero")

        