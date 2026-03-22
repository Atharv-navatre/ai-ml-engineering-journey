'''
Let’s create a “ ”. Given a secret number (already
decided by you), write a program that asks the user to guess it and prints:
Q10 Number Guessing Game
•
"Too high" if the guess is above the number
•
"Too low" if the guess is below
•
"Correct!" if the guess matches
'''

# Number Guessing Game

secret_number = 7  # you can change this

while True:
    guess = int(input("Guess the number: "))

    if guess > secret_number:
        print("Too high")
    elif guess < secret_number:
        print("Too low")
    else:
        print("Correct!")
        break