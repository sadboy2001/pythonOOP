import math

from figure_abs  import Figure


class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c):
        if (
            side_a <= 0 or
            side_b <= 0 or
            side_c <= 0 or
            side_a >= side_b + side_c or
            side_b >= side_c + side_a or
            side_c >= side_a + side_b
                ):
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
