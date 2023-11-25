import pytest

from src.rectangle import Rectangle
from src.square import Square
from src.triangle import Triangle
from src.circle import Circle


@pytest.mark.parametrize('radius, perimeter, area',
                         [
                             (5, 31.4, 79),
                             (10, 62.8, 314),
                         ])
def test_circle(radius, perimeter, area):
    r = Circle(radius)
    assert r.name == 'Circle'
    assert round(r.get_area()) == area
    assert round(r.get_perimeter(), 1) == perimeter


@pytest.mark.parametrize('radius, perimeter, area',
                         [
                             (-4, 2, -20),
                             (0, 40, 0),
                         ])
def test_circle_negative(radius, perimeter, area):
    with pytest.raises(ValueError):
        Circle(radius)


@pytest.mark.parametrize('side_a, side_b, side_c, perimeter, area',
                         [
                             (9, 7, 4, 20, 13.4),
                             (10, 8, 6, 24, 24),
                         ])
def test_triangle(side_a, side_b, side_c, perimeter, area):
    r = Triangle(side_a, side_b, side_c)
    assert r.name == 'Triangle'
    assert round(r.get_area(), 1) == area
    assert r.get_perimeter() == perimeter


@pytest.mark.parametrize('side_a, side_b, side_c',
                         [
                             (-4, 5, 3),
                             (0, 20, 2),
                         ])
def test_triangle_negative(side_a, side_b, side_c):
    with pytest.raises(ValueError):
        Triangle(side_a, side_b, side_c)


@pytest.mark.parametrize('side_a, side_b, perimeter, area',
                         [
                             (4, 5, 18, 20),
                             (10, 20, 60, 200),
                         ])
def test_rectangle(side_a, side_b, perimeter, area):
    r = Rectangle(side_a, side_b)
    assert r.name == 'Rectangle'
    assert r.get_area() == area
    assert r.get_perimeter() == perimeter


@pytest.mark.parametrize('side_a, side_b, perimeter, area',
                         [
                             (-4, 5, 2, -20),
                             (0, 20, 40, 0),
                         ])
def test_rectangle_negative(side_a, side_b, perimeter, area):
    with pytest.raises(ValueError):
        Rectangle(side_a, side_b)


@pytest.mark.parametrize('side_a, perimeter, area',
                         [
                             (4, 16, 16),
                             (10, 40, 100),
                         ])
def test_square(side_a, perimeter, area):
    r = Square(side_a)
    assert r.name == 'Square'
    assert r.get_area() == area
    assert r.get_perimeter() == perimeter


@pytest.mark.parametrize('side_a', [-10, 0])
def test_square_negative(side_a):
    with pytest.raises(ValueError):
        Square(side_a)


def test_add_area():
    r1 = Rectangle(10, 5)
    r2 = Circle(8)
    assert round(r1.add_area(r2)) == 251


def test_add_area_negative():
    r1 = Rectangle(10, 5)
    r2 = Circle(5)
    assert r1.add_area(r2) == 75
