'''
Q5. Create a dictionary where:
• Keys = student names
• Values = marks (integer)
Write a menu-based program where user presses a key (’A’, ‘B’, ‘C’, ‘D’)
depending on the operation they want to perform on the dictionary:
1. A - Add a student
2. B - Update marks
3. C - Search for a student
4. D - Display all students and marks
'''

students = {}

while True:
    print("\nMenu:")
    print("A - Add Student")
    print("B - Update Marks")
    print("C - Search Student")
    print("D - Display All")
    print("E - Exit")

    choice = input("Enter your choice: ").upper()

    if choice == 'A':
        name = input("Enter student name: ").lower()
        marks = int(input("Enter marks: "))
        students[name] = marks
        print("Student added!")

    elif choice == 'B':
        name = input("Enter student name to update: ").lower()
        if name in students:
            marks = int(input("Enter new marks: "))
            students[name] = marks
            print("Marks updated!")
        else:
            print("Student not found!")

    elif choice == 'C':
        name = input("Enter student name to search: ").lower()
        if name in students:
            print("Marks:", students[name])
        else:
            print("Student not found!")

    elif choice == 'D':
        if len(students) == 0:
            print("No data available")
        else:
            for name, marks in students.items():
                print(name, ":", marks)

    elif choice == 'E':
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Try again.")