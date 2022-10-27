class student:
    def __init__(self,name,id,course):
        self.name=name
        self.id=id
        self.courses=[]
        for items in course:
            self.courses.append(items)
    def get_course(self):#之所以需要self参数是因为
        for item in self.courses:
            print("学生选了 %s 课程" % item)
    def __str__(self):
        return "学生的姓名：%s\n学生的学号：%s" % (self.name,self.id)
    def __len__(self):
        print("学生一共学了",len(self.courses),"门课")
        return False
student1=student("XM","122",["Math","English","Science"])
print(student1)
student1.get_course()
len(student1)
