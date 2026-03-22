"""color = input("Enter color: ")

if color == "red":
    print("Stop")
elif color == "green": 
    print("GO")
elif color  == "Yellow":
    print("Look")  
else:         
    print("Wrong color for tracffic lights")"""

'''age = int(input("Enter age: "))

if (age < 13):
    print("Child")
elif (age >= 13 and age < 18): #13-18
    print("Teenager")    
elif age > 18:
    print("adult")      
else:
    print("Enter correct val.")    '''

'''username = input("Enter Username")
Password = input("Enter Password")

if username == "admin" and Password == "pass":
    print("Login sucessful")
elif (username != "admin"):
    print("Wrong Username")
else:
    print("Wrong password")      ''' 

'''n = int(input("enter num: "))

if (n % 5 == 0):
    print("Multiple of 5")
else:
    print("Not multiple of 5")
'''

'''n = int(input("enter num: "))

if (n % 2 == 0):
    print("even")
else:
    print("odd")'''


'''username = input("Enter Username: ")
Password = input("Enter Password: ")

if username == "admin" and Password == "pass":
    print("Login sucessful")
else:
  if (username != "admin"):
    print("Wrong Username")
  else:
    print("Wrong password") '''

'''color = input("Enter color: ")

match color:
    case "Green":
        print("Go")
    case "Red":
        print("Stop")
    case "Yellow":
        print("Look")
    case _:
        print("Enter correct color!") '''  

'''#infinite loop

while True:
    print("Hello world")  '''

'''count = 1 #iterator used for to run loop (instead of count we use , i & j like that)

while count <= 5:
    print("HI",count)
    count += 1
    print("after loop counter = ", count) #6'''

'''i =1 
while i <= 5:
    print(i)
    i += 1'''
    
'''
i=5
while i >= 1:
    print(i)
    i -= 1'''

#multiplication of any num

'''n = int(input("enter num: "))

i = 1
while (i<=10):
    print(n*i)
    i +=1'''

'''n = int(input("enter num: "))

i = 0
while (i<10):
    print(n*(i+1))
    i +=1
'''

'''i = 1

while (i<=10):
    if (i%6==0):
        break
    print(i)
    i +=1

print("outside loop now...")    '''

'''i = 1

while (i<=10):
    if (i%3==0):
        i +=1
        continue
    print(i)
    i +=1

print("outside loop now...")    '''

#odd nums

'''i = 0

while (i<10):
       i +=1
       if (i%2==0):
        continue
       print(i)

print("outside loop now...")    '''

'''string = "hello"

if 'o' in string:
    print("o exists in string")'''
    # for var in string:
    #     print(var)

    #in- membership operator(to check the presence of word)


'''word = "artificial intelligence"

count = 0

for ch in word:
    if(ch == 'i'):
        count += 1

print("count of i =", count)       ''' 

#print vowel of given string

'''word = "artificial"

count = 0

for ch in word:
    if(ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'):
         count += 1
         print("ans: ", count)       
'''

#range function
'''
for i in range(1,10,2):
    print(i)
'''

#sum of n nummbers
'''n = int(input("enter num: ")) 

sum = 0

for i in range(1, n+1):
    sum += i

print("sum: ", sum)  '''

#function it is used for reuse in logic (share input values and gives logic to the output)

# def hello():    
#     print("Hello")

# hello()

'''def sum(a,b): #parameters
    s = a + b
    return s

#function call 
ans=sum(3,4) #arguments
print(ans)'''


'''def avg(a,b,c):
    s = a+b+c
    return s/3
print(avg(2,2,2))'''

'''def sum(a, b=1):
    return a+b
print(sum(5))'''

#Lambda
'''avg = lambda a,b: (a+b)/2
print(avg(3,3))'''

#Factorial

def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i

        return fact
    
    n = int(input("Enter n: ")) 
    print(cal_fact(n))
