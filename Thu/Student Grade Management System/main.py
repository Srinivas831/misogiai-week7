from collections import defaultdict

class GradeManager:
    def __init__(self):
        """
        Initialize the grade manager with appropriate defaultdict structures.
        """
        self.data = defaultdict(lambda: defaultdict(list))
        
    def add_grade(self, student_name, sub, grade):
        """
        """
        self.data[student_name][sub].append(grade)
    
    
#     self.data["Alice"] = {
#     "Math": [85, 90],
#     "Science": [92],
#     "English": [78]
# }

    
    def get_avg(self, student_name):
        if student_name not in self.data:
            return 0
        tot=0
        count = 0
        for i in self.data[student_name].values():
            print("iii",i)
            tot+=sum(i)
            count += len(i)
        return tot/count
        
        
    def get_subject_statistics(self, subject):
        grades = []

        for student in self.data:
            if subject in self.data[student]:
                grades.extend(self.data[student][subject])

        if not grades:
            return {
            'average': 0,
            'highest': 0,
            'lowest': 0,
            'student_count': 0
        }

        return {
        'average': sum(grades) / len(grades),
        'highest': max(grades),
        'lowest': min(grades),
        'student_count': sum(1 for student in self.data if subject in self.data[student])
    }

        
        
        
manager = GradeManager()

manager.data["Alice"]["Math"].append(85)
manager.data["Alice"]["Math"].append(50)
manager.data["Alice"]["Science"].append(92)
print(manager.data)
print(manager.get_avg("Alice"))


# print(defaultdict(lambda: defaultdict(list)))

# print("Alice avg", manager.get_student_average("Alice"))