class Exam:
    def __init__(self,id,start_time,end_time,points):
        self.__start_time=start_time
        self.__end_time=end_time
        self.points=points
        self.id=id
class Test(Exam):
    def __init__(self):
        self.points=10