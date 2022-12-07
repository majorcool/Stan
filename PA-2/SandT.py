class Student:
    def __init__(self):
        self.UserName=str()
        self.PassWord=str()
        self.learn_score=0
        self.cls_picked=[]
        self.UserType='Student'
    def Login_(self):
        return self.UserName,self.PassWord