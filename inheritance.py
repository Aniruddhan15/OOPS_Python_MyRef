from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def work(self):
        pass

    def __eq__(self, other):
        return self.name == other.name

class Developer(Employee):
    def work(self):
        print(f"{self.name} writes code.")

class Manager(Employee):
    def work(self):
        print(f"{self.name} manages the team.")

class Team:
    def __init__(self):
        self.members = []

    def add_member(self, emp: Employee):
        self.members.append(emp)

    def team_work(self):
        for emp in self.members:
            emp.work()  # Polymorphism: work() is different based on object

dev1 = Developer("Alice")
dev2 = Developer("Bob")
mgr = Manager("Carol")

team = Team()
team.add_member(dev1)
team.add_member(dev2)
team.add_member(mgr)

team.team_work()

print(dev1 == Developer("Alice"))  # True due to __eq__ overriding
