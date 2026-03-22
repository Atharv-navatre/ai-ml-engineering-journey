'''
. Write a program that takes as input. Using conditional statements,
calculate the final tax rate based on these rules:

• If salary < 30,000 → 5%
• If salary is 30,000–70,000 → 15%
• If salary > 70,000 → 25%
'''

sal = float(input("Enter salary: "))

if  sal < 30000:
    tax_rate = 5  
elif 30000 <= sal <= 70000:
    tax_rate = 15
else:
    tax_rate = 25

tax = sal * (tax_rate/100)

print("salary: ",sal)
print("tax rate: ",tax_rate, "%")
print("tax amount: ",tax)
   







