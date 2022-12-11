import Educational_administrator
import Courses
import SandT
class System:
    UserType=''
    Class_able={}
    Student_pick_cls={}
    Student_score_needed=int()
    Student_acc={}
    Student_user=[]
    def __init__(self):
        pass

    def Check_score(self): #Student
        if System.UserType=='Student':
            return "您的学分为%s" % self.learn_score
        else:
            print("您不是学生或者未登录")
            return False
    def Pick_cls(self): #Student
        if System.UserType=='Student':
            Cls_picked=input('输入想要选择的课程的名字')
            if Cls_picked not in System.Class_able:
                print("暂无此课程")
                return False
            elif Cls_picked in System.Student_pick_cls[self.UserName]:
                print("已选择此课程")
                return False
            elif System.Class_able[Cls_picked].storage==0:
                print("此课程已满员")
                return False
            else:
                System.Student_pick_cls[self.UserName].append(Cls_picked)
                print("已成功报名%s课程" % Cls_picked)
        else:
            print("您不是学生或者未登录")
    def Quit_cls(self): #Student
        if System.UserType=='Student':
            select_quit_cls=input("输入你想退课的课程名称")
            if select_quit_cls not in System.Student_pick_cls[self.UserName]:
                print("您没有报这一门课")
                return False
            else:
                submit_quit_cls=input("您确认要退课吗,请输入'确认'")
                if submit_quit_cls=="确认":
                    print(self.UserName)
                    System.Student_pick_cls[self.UserName].pop(System.Student_pick_cls[self.UserName].index(select_quit_cls))
                    print(System.Student_pick_cls)
                    print("退课成功")   #这边缺一个课程名额+1
                else:
                    print("退课失败")
        else:
            print("您不是学生或者未登录")
    def Check_acc(self): #EA
        if System.UserType=="EA":
            check_acc_name=input("输入你想查询的账号名:")
            if check_acc_name not in System.Student_acc.keys():
                print("没查询到此账号")
                return False
            else:
                print("账号用户名:%s" % check_acc_name)
                print("账号密码:%s" % System.Student_acc[check_acc_name])
        else:
            print("您不是教务或者未登录")
            return False
    def Create_acc(self): #EA
        if System.UserType=="EA":
            acc_name=input("输入账号名字")
            self.ACC_Username=[]
            for index,items in enumerate(self.Stu_account):
                if index%2==0:
                    self.ACC_Username.append(items)
            if acc_name in self.ACC_Username:
                print("此账号已存在")
                return False
            file=open('Student accounts',mode='a')
            file.write(acc_name+'\n')
            self.Stu_account.append(acc_name)
            acc_psw=input("请输入账号密码")
            file.write(acc_psw+'\n')
            self.Stu_account.append(acc_psw)
            file.close()
        else:
            print("您不是教务或者未登录")
            return False
    def Set(self): #EA
        if System.UserType=="EA":
            file=open('Student_score_needed', mode='r')
            student_score=file.readline()
            student_score=student_score.rstrip()
            System.Student_score_needed=input("请输入学生需要的学分,原先学分为%s" % student_score)
            file.close()
            file=open('Student_score_needed',mode="w+")
            file.write(System.Student_score_needed)
            file.close()
            print("修改成功")
        else:
            print("您不是教务或者未登录")
            return False
    def Create_cls(self): #EA
        if System.UserType=="EA":
            file=open("Classes available",mode="r+")
            temp=file.readlines()
            for items in temp:
                if items[0]=='N'and items[1]=="a" and items[2]=='m' and items[3]=="e":
                    if
            self.cls_name=input("输入课程名")
            self.app_cls_name=self.cls_name
            self.cls_teacher=str(input("输入老师名字"))
            self.cls_score=int(input("输入课程学分"))
            self.cls_must=bool(input("输入True或False,课程是否是必选?"))
            self.cls_storage=int(input("输入课程容量"))
            if self.cls_name in System.Class_able:
                print("已有此课程")
                return False
            self.cls_name=Courses.Class(self.cls_name,self.cls_teacher,self.cls_score,self.cls_must,self.cls_storage)
            System.Class_able[self.app_cls_name]=self.cls_name
        else:
            print("您不是教务或者未登录")
            return False
    def Change_cls(self): #EA
        if System.UserType=="EA":
            self.change_cls_inf_name=input("请输入想要修改信息的课程的名称")
            if self.change_cls_inf_name in System.Class_able.keys():

                self.change_cls_inf=input("请输入你想修改的课程的信息(1-5),如果想修改多个就请输入多个数字，比如12\n1:课程名称\n2:课程老师名字\n3:课程学分\n4:课程是否为必修\n5:课程剩余容量")
                if '1' in self.change_cls_inf:
                    print("课程原名称为%s" % System.Class_able[self.change_cls_inf_name].name)
                    Origin_name=System.Class_able[self.change_cls_inf_name].name
                    System.Class_able[self.change_cls_inf_name].name=input("请输入你想更改的课程名称")
                    New_name=System.Class_able[self.change_cls_inf_name].name
                    System.Class_able[New_name]=System.Class_able.pop(Origin_name)
                if '2' in self.change_cls_inf:
                    print("课程老师原名称为%s" % System.Class_able[self.change_cls_inf_name].teacher)
                    System.Class_able[self.change_cls_inf_name].teacher=input("请输入你想更改的课程老师名称")
                if '3' in self.change_cls_inf:
                    print("课程原学分为%s" % System.Class_able[self.change_cls_inf_name].score)
                    System.Class_able[self.change_cls_inf_name].score=int(input("请输入你想更改的学分"))
                if '4' in self.change_cls_inf:
                    print("课程的必修的选项的为%s" % System.Class_able[self.change_cls_inf_name].must)
                    System.Class_able[self.change_cls_inf_name].must=bool(input("请输入你想更改的必修选项(True/False)"))
                if '5' in self.change_cls_inf:
                    print("课程原剩余容量为%s" % System.Class_able[self.change_cls_inf_name].storage)
                    System.Class_able[self.change_cls_inf_name].storage=input("请输入你想更改的剩余容量")
            else:
                print("暂无此课程")
                return False
        else:
            print("您不是教务或者未登录")
            return False
    def Check_stu_cls(self): #EA
        if System.UserType=="EA":
            self.search_student_cls_name=input("请输入想要查询所选课程的学生的名字:")
            if self.search_student_cls_name in System.Student_pick_cls.keys():
                print("该学生选了",System.Student_pick_cls[self.search_student_cls_name],'课程')
            else:
                print("未查询到此学生")
                return False
        else:
            print("您不是教务或者未登录")
            return False
    def Login(self): #EA,Student
        file1=open('EA Account.txt', mode='r')
        file2=open('Student accounts',mode='r')
        self.EA_account=[]
        self.Stu_account=[]
        length_file=file1.readlines()
        for items in length_file:
            self.EA_account.append(items.rstrip())
        length_file=file2.readlines()
        for items in length_file:
            self.Stu_account.append(items.rstrip())
        file1.close()
        file2.close()
        get_username=input('请输入用户名?')
        get_psw=input("输入密码")
        for i in range(len(self.EA_account)-1):
            if self.EA_account[i]==get_username and self.EA_account[i+1]==get_psw:
                print('登陆成功')
                System.UserType='EA'
                return True
        for i in range(len(self.Stu_account)-1):
            if self.Stu_account[i]==get_username and self.Stu_account[i+1]==get_psw:
                print('登陆成功')
                System.UserType='Stu'
                return True
        print("登陆失败")
        return False


    def Log_out(self):
        if System.UserType=='':
            print("未登录")
            return False
        System.UserType=''
        print("已登出")
    def Check_cls(self): #EA,Student
        if System.UserType=="EA" or System.UserType=="Student":
            self.cls_search_name=input("输入你想查询的课程的名字:")
            if self.cls_search_name not in System.Class_able:
                print("无此课程")
                return False
            print('课程的名字:',System.Class_able[self.cls_search_name].name)
            print("课程的老师:",System.Class_able[self.cls_search_name].teacher)
            print("课程的学分:",System.Class_able[self.cls_search_name].score)
            print("课程是否为必修课:",System.Class_able[self.cls_search_name].must)
            print('课程剩余容量:',System.Class_able[self.cls_search_name].storage)
        else:
            print("请先登录")
            return False
system=System()
system.Login()
system.Set()
'''
EA=Educational_administrator.E_A("EA","123")
Student=SandT.Student()
System.Login(EA)
System.Set(EA)
System.Create_acc(EA)
System.Create_cls(EA)
System.Log_out(EA)
System.Login(System.Student_user[0])
System.Pick_cls(System.Student_user[0])
System.Quit_cls(System.Student_user[0])
System.Log_out(System.Student_user[0])
System.Login(EA)
System.Check_stu_cls(EA)
'''
'''
System.Create_cls(EA)
System.Change_cls(EA)
System.Check_cls(EA)
System.Log_out(EA)
Stu1=SandT.Student("Stu1","123")
System.Login(Stu1)
System.Pick_cls(Stu1)
System.Log_out(Stu1)
System.Login(EA)
System.Check_stu_cls(EA)
'''
