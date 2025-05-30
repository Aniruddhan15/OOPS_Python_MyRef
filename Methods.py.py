class Employee:
    raise_amount = 1.05
    emp_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.emp_count += 1
    
    @classmethod    
    def apply_raise(cls,self):
        self.salary = int(self.salary * cls.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    
    def from_string(self, emp_str):
        name, salary = emp_str.split("-")
        return (self.name, int(self.salary))

# Create instance
emp1 = Employee("Alice", 50000)

print(emp1.salary)  # 50000

# Change raise amount using class method
print(Employee.apply_raise())
print(Employee.set_raise_amount(3))
print(emp1.from_string("Alice-455000"))
# 55000 (50000 * 1.10)
