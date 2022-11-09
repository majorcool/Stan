class Exam:
    def __init__(self):
        self.__start_time='5:00'
        self.__end_time='7:00'
        self.points=21
        self.id=8
class Test(Exam):
    def __init__(self):
        super() .__init__()
        self.points=10
        print(self.points)
        print(self.id)
b=Test()