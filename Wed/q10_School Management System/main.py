school = {
    "Math": {
        "teacher": "Mr. Smith",
        "students": [("Alice", 85), ("Bob", 92), ("Carol", 78)]
    },
    "Science": {
        "teacher": "Ms. Johnson",
        "students": [("David", 88), ("Eve", 94), ("Frank", 82)]
    }
}


# terate through all classes and print the name of each teacher.
for key in school:
    # print(key)
    print(f"{key}:{school[key]["teacher"]}")


 # For each class, calculate and display the average grade of the students.
for key in school:
    students = school[key]["students"]
    avg = 0
    tot=0
    for i in students:
        tot = tot+i[1]
    avg = tot/len(students)
    print(f"Avg for {key} is: {avg}")


    # Identify the student with the highest grade among all students across every class.
max = float("-inf")
student = None
for sub, detail in school.items():
        stdArr = detail["students"]
        for i in stdArr:
                if i[1]>max:
                        max = i[1]
                        student= i[0]
print(max) 
print(student) 

