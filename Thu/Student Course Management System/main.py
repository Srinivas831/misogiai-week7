class Course:
    def __init__(self, course_code, title, instructor, credits, capacity):
        self.course_code = course_code
        self.title = title
        self.instructor = instructor
        self.credits = credits
        self.capacity = capacity
        self.enrolled_students = []
        self.grades = {}
        self.waitlist = []

    def get_available_spots(self):
        return self.capacity - len(self.enrolled_students)

    def get_enrollment_count(self):
        return len(self.enrolled_students)

    def add_grade(self, student_id, grade):
        self.grades[student_id] = grade

    def get_course_statistics(self):
        if not self.grades:
            return {
                'average': 0,
                'highest': 0,
                'lowest': 0,
                'student_count': 0
            }

        scores = list(self.grades.values())
        return {
            'average': sum(scores) / len(scores),
            'highest': max(scores),
            'lowest': min(scores),
            'student_count': len(scores)
        }

    def is_full(self):
        return len(self.enrolled_students) >= self.capacity
