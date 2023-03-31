class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"
    def set_width(self, width):
        self.width = width
    def set_height(self, height):
        self.height = height
    def get_area(self):
        return (self.width * self.height)
    def get_perimeter(self):
        return (2 * self.width + 2 * self.height)
    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** .5)
    def get_picture(self):
        lines = []
        picture = ""
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        for line in range(self.height):
            lines.append("*" * self.width)
        for i in lines:
            picture += f'{"".join(i)}\n'
        return picture

    def get_amount_inside(self, object):
        selfArea = self.get_area()
        parameterArea = object.get_area()
        if self.width < object.width or self.height < object.height:
            return 0
        fit = int(selfArea / parameterArea)
        return fit

class Square(Rectangle):
    def __init__(self, lenght):
        self.height = lenght
        self.width = lenght
    def __str__(self):
        return f"Square(side={self.width})"    
    def set_side(self, lenght):
        self.height = lenght
        self.width = lenght



rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))