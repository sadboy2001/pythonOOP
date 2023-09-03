from abc import ABC, abstractmethod
import math


class Figure(ABC):

    @abstractmethod
    def get_area(self):
        pass

    def add_area(self, other_figure):
        if isinstance(other_figure, Figure):
            return self.get_area() + other_figure.get_area()
        raise ValueError(f'Object {other_figure} is not Figure')


class Circle(Figure):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError(f'Can not create Circle')
        self.radius = radius
        self.name = 'Circle'

    def get_area(self):
        return math.pi * self.radius * self.radius

    def get_perimeter(self):
        return 2 * math.pi * self.radius


class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c):
        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError(f'Can not create Triangle')
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.name = 'Triangle'

    def get_area(self):
        s = (self.side_a + self.side_b + self.side_c)/2
        return math.sqrt(s*(s - self.side_a) * (s - self.side_b) * (s-self.side_c))

    def get_perimeter(self):
        return self.side_b + self.side_a + self.side_c


class Rectangle(Figure):
    def __init__(self, side_a, side_b):
        if side_a <= 0 or side_b <= 0:
            raise ValueError(f'Can not create Rectangle')
        self.side_a = side_a
        self.side_b = side_b
        self.name = 'Rectangle'

    def get_area(self):
        return self.side_a * self.side_b

    def get_perimeter(self):
        return 2 * (self.side_a + self.side_b)


class Square(Rectangle):
    def __init__(self, side_a):
        if side_a <= 0:
            raise ValueError(f'Can not create Square')
        super().__init__(side_a, side_a)
        self.side_a = side_a
        self.name = 'Square'
