class Ellipse():
    pass
class Circle(Ellipse):
    def perimeter(self):
        return self.r*3.14*2
    def area(self):
        return self.r**2*3.14