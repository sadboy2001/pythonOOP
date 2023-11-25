from figure_abs  import Figure


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
