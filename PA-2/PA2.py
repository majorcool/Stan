class User:
    def __init__(self):
        self.type='user'
    def Print_type(self):
        return self.type
    def Login(self):
        pass
    def Check_cls(self):
        pass
class Educational_administrator(User):
    def Check_acc(self):
        pass
    def Create_acc(self):
        pass
    def Set(self):
        pass
    def Create_cls(self):
        pass
    def Change_cls(self):
        pass
    def Check_stu_cls(self):
        pass
class Student(User):
    def __init__(self):
        super(Student, self).__init__()
        self.learn_score=0
        self.cls_picked=''
    def Check_score(self):
        return self.learn_score
    def Pick_cls(self):
        pass
    def Quit_cls(self):
        pass
class Class:
    def __init__(self):
        self.must=bool()
        self.score=0
        self.teacher=str()
        self.name=str()
        self.storage=int()
    def cls_information_get(self):
        return '是否为必选课:',self.must,'课程学分:',self.score,'课程老师:',self.teacher,'课程名字',self.name,'课程容量',self.storage