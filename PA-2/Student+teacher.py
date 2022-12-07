import control_system
class Student(control_system.System):
    def __init__(self,UserName,PassWord):
        self.UserName=UserName
        self.PassWord=PassWord
        self.learn_score=0
        self.cls_picked=''
