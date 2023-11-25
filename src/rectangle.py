from figure_abs import Figure


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



