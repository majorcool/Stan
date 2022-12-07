class Class:
    def __init__(self):
        self.must=bool()
        self.score=0
        self.teacher=str()
        self.name=str()
        self.storage=int()
    def cls_information_get(self):
        return '是否为必选课:',self.must,'课程学分:',self.score,'课程老师:',self.teacher,'课程名字',self.name,'课程容量',self.storage