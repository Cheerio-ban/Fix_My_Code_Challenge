#!/usr/bin/python3
"""Represents a Square."""


class Square():
    """
    Represents a square
    """
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """Initializes the class"""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """Area of the square"""
        return self.width * self.height

    def perimeter_of_my_square(self):
        """Perimeter of the square class"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """Prints the square class"""
        return "{}/{}".format(self.width, self.width)


if __name__ == "__main__":
    """Creates an instance of the square class"""
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
