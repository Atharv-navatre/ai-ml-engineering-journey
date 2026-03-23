'''Q1. Ask the user for a string and check whether it is a palindrome or not.
A is a string which is same when we read it forward & backward. Eg -
“madam”, “racecar” etc.
palindrome
[ - A palindrome string is equal to the reversed version of the string. We can
use a loop to reverse the string manually. ]'''

word = input("Enter a string: ")

reverse = ""

for char in word:
    reverse = char + reverse

if word == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")