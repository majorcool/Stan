class Course:
    def __init__(self,name,student_number,grade):
        self.name=name
        self.student_number=student_number
        self.grade=grade
    def __len__(self):
        return "一共有%d学生选了这门课" % (self.student_number)
    def choose(self):
        classes=input("输入你想选的课")
        print("你选了%s" % (classes))