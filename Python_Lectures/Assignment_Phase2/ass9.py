'''
Write a function that returns if is a prime number and
otherwise, using a loop.
Q9 is_prime(n) True n
False
[Hint -
1. We only check prime for 2 or numbers greater than 2. is the smallest
prime number.
2
2. A number, , will always get divided by atleast one number in
range [2, n-1].
non-Prime n
Eg - For number we’ll check in range (2, 8) & it’ll get divided by 3. So is
non-prime & we’ll return false for it.
9 9
For number 7     we’ll check in range (2, 6) & it won’t get divided by any. So 7
is prime & we’ll return true for it. ]
'''

def is_prime(n):
    if n <= 1:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False
    
    return True

# taking input
num = int(input("Enter a number: "))

if is_prime(num):
    print("Prime number")
else:
    print("Not a prime number")