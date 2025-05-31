
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self): pass

    @abstractmethod
    def perimeter(self): pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __str__(self):
        return f"Circle with radius {self.radius}"

class Rectangle(Shape):
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def area(self):
        return self.l * self.b

    def perimeter(self):
        return 2 * (self.l + self.b)

    def __str__(self):
        return f"Rectangle {self.l}x{self.b}"

r = Rectangle(4, 5)
c1 = Circle(7)
c2 = Circle(7)

print(r)
print(f"Area: {r.area()}, Perimeter: {r.perimeter()}")
print(c1)
print(f"Equal Circles? {c1 == c2}")
