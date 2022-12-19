import Maaath
class Point:
    def __init__(self):
        self.x = [9,10]
        self.y=[9,12]
    def _distance(self):
        print('距离为%.3f' %(math.sqrt((self.x[1]-self.x[0])**2+(self.y[1]-self.y[0])**2)))
class Segment(Point):
    def __init__(self):
        super().__init__()
        self.__p1=[self.x[0],self.y[0]]
        self.__p2=[self.x[1],self.y[1]]
    def get_len(self):
        super()._distance()
a=Segment()
a._distance()