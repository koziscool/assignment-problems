
import math
import matplotlib.pyplot as plt
plt.style.use('bmh')

class Shape:
    def __init__(self, base, height, color):
        self.base = base
        self.height = height
        self.color = color

    def describe(self):
        print("Base: ", self.base)
        print("Height: ", self.height)
        print("Color: ", self.color)
        print("Perimeter: ", self.perimeter)
        print("Area: ", self.area)
        print("Vertices: ", self.vertices)
        print()

    def render(self):
        x_values = [ i for i,j in self.vertices ] + [ self.vertices[0][0] ]
        y_values = [ j for i,j in self.vertices ] + [ self.vertices[0][1] ] 
        plt.plot(
            x_values, 
            y_values,
            color=self.color
        )
        plt.gca().set_aspect("equal")
        plt.savefig(self.plot_filename)
        plt.clf()

class Rectangle(Shape):
    def __init__(self, base, height, color):
        super().__init__(base, height, color)

        self.perimeter = 2 * self.base + 2 * self.height
        self.area = self.base * self.height
        self.vertices = [ (0,0), (self.base, 0), (self.base, self.height), (0, self.height) ]
        self.plot_filename = "rectangle.png"


class RightTriangle(Shape):
    def __init__(self, base, height, color):
        super().__init__(base, height, color)

        self.perimeter = self.base +  self.height + math.sqrt(self.base**2 + self.height**2)
        self.area = self.base * self.height / 2
        self.vertices = [ (0,0), (self.base, 0), (0, self.height) ]
        self.plot_filename = "triangle.png"


class Square(Rectangle):
    def __init__(self, side, color ):
        super().__init__(side, side, color)
        self.plot_filename = "square.png"


rect = Rectangle(5, 2, "red")
rect.describe()
rect.render()

tri = RightTriangle(5, 2, "blue")
tri.describe()
tri.render()

sq = Square( 5, 'green')
sq.describe()
sq.render()
