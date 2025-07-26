students = [
    (101, "Alice", 85, 20),
    (102, "Bob", 92, 19),
    (103, "Carol", 78, 21),
    (104, "David", 88, 20)
]
# (student_id, name, grade, age)

# Find the Student with the Highest Grade
# max=float("-inf")
# for i in students:
#     # print(students[i])
#     if i[2]>max:
#         max = i[2]
# print(max)


max(students, key=lambda student : students[2])



new_list = list()
for i in students:
    new_list.append((i[1], i[2]))

print(new_list)


try:
  students[0][1] = "Anna"
except TypeError as e:
   print("Error:",e)

print(students)



