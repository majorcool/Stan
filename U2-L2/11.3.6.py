class student:
    def __init__(self,id,name,courses:list):
        self.id=id
        self.name=name
        self.courses=courses
    def add_course(self,courseid):
        self.courses.append(courseid)
        print(self.courses)
    def del_course(self,courseid):
        if courseid in self.courses:
            del self.courses[self.courses.index(courseid)]
            print(self.courses)
        else:
            print("没有此课程")
class course:
    def __init__(self,id,name,students):
        self.id=id
        self.name=name
        self.students=students
    def add_student(self,studentid):
        self.students.append(studentid)
        print(self.students)
    def del_student(self,studentid):
        if studentid in self.students:
            del self.students[self.students.index(studentid)]
            print(self.students)
        else:
            print("没有此学生")
xm=student(9,'xm',['kk'])
xm.add_course('djsd')
xm.del_course('djsd')
ela=course(9,"English",['x'])
ela.add_student('jash')


