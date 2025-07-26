employees = [
    ("Alice", 50000, "Engineering"),
    ("Bob", 60000, "Marketing"),
    ("David", 45000, "Sales"),
    ("Carol", 55000, "Engineering")
]


ascending = sorted(employees, key=lambda x:x[1])
print(ascending)
descending = sorted(employees, key=lambda emp: emp[1], reverse=True)


by_name = sorted(employees, key=lambda x:x[2])
final = sorted(by_name, key=lambda x:x[1])
print(final)
sorted_employees = sorted(employees, key=lambda emp: (emp[2], emp[1]))



rev = employees[::-1]