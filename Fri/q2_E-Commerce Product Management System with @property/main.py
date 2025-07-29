from datetime import datetime, timedelta
import re

class Employee:
    company_name = "GlobalTech Solutions"
    total_employees = 0
    departments = {"Engineering": 0, "Sales": 0, "HR": 0, "Marketing": 0}
    tax_rates = {"USA": 0.22, "India": 0.18, "UK": 0.25}
    next_employee_id = 1

    def __init__(self, name, department, base_salary, country, email):
        if not self.validate_email(email):
            raise ValueError("Invalid email format")
        if not self.is_valid_department(department):
            raise ValueError("Invalid department")
        
        self.name = name
        self.department = department
        self.base_salary = base_salary
        self.country = country
        self.email = email
        self.hire_date = datetime.now()
        self.performance_ratings = []

        self.employee_id = self.generate_employee_id()
        Employee.total_employees += 1
        Employee.departments[department] += 1

    @staticmethod
    def validate_email(email):
        return re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email) is not None

    @staticmethod
    def is_valid_department(dept):
        return dept in Employee.departments

    @staticmethod
    def calculate_tax(salary, country):
        return salary * Employee.tax_rates.get(country, 0.2)

    @staticmethod
    def generate_employee_id():
        year = datetime.now().year
        emp_id = f"EMP-{year}-{Employee.next_employee_id:04d}"
        Employee.next_employee_id += 1
        return emp_id

    @classmethod
    def from_csv_data(cls, csv_line):
        name, dept, salary, country, email = csv_line.split(',')
        return cls(name.strip(), dept.strip(), float(salary), country.strip(), email.strip())

    @classmethod
    def hire_bulk_employees(cls, employee_list):
        for line in employee_list:
            cls.from_csv_data(line)

    @classmethod
    def get_department_stats(cls):
        return {dept: {"count": count} for dept, count in cls.departments.items()}

    @classmethod
    def set_tax_rate(cls, country, rate):
        cls.tax_rates[country] = rate

    def add_performance_rating(self, rating):
        if not (1 <= rating <= 5):
            raise ValueError("Rating must be between 1 and 5")
        self.performance_ratings.append(rating)

    def get_average_performance(self):
        if not self.performance_ratings:
            return 0
        return round(sum(self.performance_ratings) / len(self.performance_ratings), 2)

    def get_years_of_service(self):
        delta = datetime.now() - self.hire_date
        return delta.days // 365

    def is_eligible_for_bonus(self):
        return self.get_average_performance() > 3.5 and self.get_years_of_service() > 1

    def calculate_net_salary(self):
        return round(self.base_salary - self.calculate_tax(self.base_salary, self.country), 2)
