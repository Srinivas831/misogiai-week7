# Grade Analyzer
grades = [85, 92, 78, 90, 88, 76, 94, 89, 87, 91]

sliced = grades[2:7]
# print(sliced)

grades_abv_85 = [i for i in grades if i>85]
print(grades_abv_85)


grades[3] =95

grades.append(10)
grades.append(20)
grades.append(30)


# sort = grades.sort()
sort = sorted(grades, reverse=True)
print("sorting",sort)

top_5 = sort[:5]
print(top_5)

print(grades)