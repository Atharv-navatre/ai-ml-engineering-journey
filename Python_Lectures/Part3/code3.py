'''#string

word = "Python"
word2 = "is my favorite"
# print(len(word))

# print(word+" "+word2)
print(word[2])'''


'''#slicing

word ="I love to coding"

# print(word[10:13])

# print(word[10:])

# print(word[10:len(word)])'''

'''#formatting

a=5
b=10
sum=a+b

#normal formatting
print("language is {}".format("Python"))
print("sum of {} & {} is {}".format(a,b,sum))
#index based formatting
print("sum of {1} & {0} is {2}".format(a,b,sum))'''

'''#f-string - Literal string interpolation

a=10
b=5

print(f"avg of {a} & {b} is {a+b/2}")'''

'''#List

marks = [99,92,83,93,"abc",3.12]

print(marks[4])'''

'''#List

num=[1,2,3,4,5]

num.append(7)
print(num)

num.insert(3,10)
print(num)

num.sort(reverse=True)
print(num)

num.sort
print(num)

num.reverse
print(num)'''

#Loop with string

'''nums = [1,2,3,10,4]

x=10
idx=0

for val in nums:
    if(val == x):
        print(f"{x} found at indx={idx}")
        break
    idx += 1'''


'''#tuple

tup = (1,2,3,4,5)

sum = 0
for val in tup:
    sum += val

print(f"sum of val is {sum}")    '''


'''tup = (1,2,3,2,2,4)

print(tup.index(2))
print(tup.count(2))'''

#dict

'''info ={

    "name":"Atharv",
    "cgpa": 9.3,
    "subjects": ["math","science"]
}
info["cgpa"]=9.8

print(info["cgpa"])'''

'''info ={

    "name":"Atharv",
    "cgpa": 9.3,
    "subjects": ["math","science"]
}
print(info.get("cgpa2"))

print("end of code")'''


#sets

'''s = {1,2,3,4,2}

# print(s)
# print(len(s))
# s.add(8)
# print(s)
# s.remove(2)
# print(s)

# s.clear()
print(s)
s.pop()
print(s)'''

'''s1 = {1,2,3,2,4,5}
s2 = {6,7,8,9,4,5}

print(s1.union(s2))
print(s1.intersection(s2))'''

'''info = [
    ("Atharv", "english"),
    ("samarth", "english"),
    ("nikhil", "math"),
    ("sanket", "physics"),
]

# courses_set = set()

# for tup in info:
#     courses_set.add(tup[1])

# print(courses_set)

for name,course in info:
    if(course == "english"):
        print(name)'''


info = [
    ("Atharv", "english"),
    ("samarth", "english"),
    ("nikhil", "math"),
    ("sanket", "physics"),
]

dict = {}

for name,course in info:
    if(dict.get(name)==None):
        dict.update({name: set()})
        dict[name].add(course)
    else:
        dict[name].add(course)  

print(dict)          
   