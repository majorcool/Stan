class Circle():
    def __init__(self,r):
        self.r=r
        self.__pi=3.14159265
    def area(self):
        print(self.__pi,self.r)
circle=Circle(3)
circle.area()