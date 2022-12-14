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
    UserName=''
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
            file=open('Classes available',mode='r')
            temp=file.readlines()
            temp2=[]#用来查询存在的课程
            for items in temp:
                if items[:4:]=="Name":
                    temp2.append(items)
            file.close()
            file2=open('Student_choosed_cls',mode="r")
            temp3=file2.readlines()
            temp4=[]#用来储存已经选择的课程
            for items in temp:
                if items[:items.find(" ")]==System.UserName:
                    temp4.append(items[items.find(" ")+1:])
            file2.close()
            Cls_picked=input('输入想要选择的课程的名字')
            file3=open('Classes available',mode="r")
            temp5=file3.readlines()
            Storage_left_cls=0
            for items in temp5:
                if items[:4:]=="Name" and items[5::]==Cls_picked:
                    Storage_left_cls=int(temp5[temp5.index(items)][5::].rstrip())
            if Cls_picked not in temp2:
                print("暂无此课程")
                return False
            elif Cls_picked in temp4:
                print("已选择此课程")
                return False
            elif Storage_left_cls==0:
                print("该课程已满员")
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
            self.cls_name=input("输入课程名")
            for items in temp:
                if items[:4:]=='Name':
                    if items[5::].rstrip()==self.cls_name:
                        print("已有此课程")
                        return False
            self.cls_teacher=str(input("输入老师名字"))
            self.cls_score=int(input("输入课程学分"))
            self.cls_must=bool(input("输入True或False,课程是否是必选?"))
            self.cls_storage=int(input("输入课程容量"))
            file.write('Name '+self.cls_name+'\n'+'Teac '+self.cls_teacher+'\n'+"Scor "+str(self.cls_score)+'\n'+"Must "+str(self.cls_must)+'\n'+"Stor "+str(self.cls_storage)+'\n')
            file.close()
        else:
            print("您不是教务或者未登录")
            return False##
    def Change_cls(self): #EA
        if System.UserType=="EA":
            file=open('Classes available',mode="r+")
            temp=file.readlines()
            temp2=[]
            for items in temp:
                if items[:4:]=='Name':
                    temp2.append(items[5::].rstrip())
            self.change_cls_inf_name=input("请输入想要修改信息的课程的名称")
            if self.change_cls_inf_name in temp2:
                self.change_cls_inf=input("请输入你想修改的课程的信息(1-5),如果想修改多个就请输入多个数字，比如12\n1:课程名称\n2:课程老师名字\n3:课程学分\n4:课程是否为必修\n5:课程剩余容量")
                if '1' in self.change_cls_inf:
                    print("课程原名称为%s" % self.change_cls_inf_name)
                    change_name=input("输入你想修改的名称")
                    for items in temp:
                        if items[:4:]=='Name' and items[5::].rstrip()==self.change_cls_inf_name:
                            temp[temp.index(items)]='Name '+change_name+'\n'
                    file2=open('Student_choosed_cls',mode="r")
                    temp3=file2.readlines()
                    for items in temp3:
                        if items[items.find(' ')+1::].rstrip()==self.change_cls_inf_name:
                            temp_name=items[:items.find(" ")+1:]
                            temp3[temp3.index(items)]=temp_name+change_name
                    file2.close()
                    file2=open('Student_choosed_cls',mode='w')
                    for item in temp3:
                        file2.write(item)
                    file2.close()
                    self.change_cls_inf_name = change_name
                if '2' in self.change_cls_inf:
                    for i in temp:
                        if i[:4:]=="Name" and i[5::].rstrip()==self.change_cls_inf_name:
                            print("课程老师原名称为%s" % temp[temp.index(i)+1][5::])
                    change_teac=input("输入你想修改的教师")
                    for i in temp:
                        if i[:4:]=="Name" and i[5::].rstrip()==self.change_cls_inf_name:
                            temp[temp.index(i)+1]="Teac "+change_teac+'\n'
                if '3' in self.change_cls_inf:
                    for i in temp:
                        if i[:4:]=="Name" and i[5::].rstrip()==self.change_cls_inf_name:
                            print("课程原学分为%s" % temp[temp.index(i)+2][5::])
                    change_scor=input("输入你想修改的学分")
                    for i in temp:
                        if i[:4:]=="Name" and i[5::].rstrip()==self.change_cls_inf_name:
                            temp[temp.index(i)+2]="Scor "+change_scor+'\n'
                if '4' in self.change_cls_inf:
                    for i in temp:
                        if i[:4:]=="Name" and i[5::].rstrip()==self.change_cls_inf_name:
                            print("课程原必修程度为%s" % temp[temp.index(i)+3][5::])
                    change_must=input("输入你想修改的必修程度")
                    for i in temp:
                        if i[:4:]=="Name" and i[5::].rstrip()==self.change_cls_inf_name:
                            temp[temp.index(i)+3]="Must "+change_must+'\n'
                if '5' in self.change_cls_inf:
                    for i in temp:
                        if i[:4:]=="Name" and i[5::].rstrip()==self.change_cls_inf_name:
                            print("课程老师原容量为%s" % temp[temp.index(i)+4][5::])
                    change_stor=input("输入你想修改的容量")
                    for i in temp:
                        if i[:4:]=="Name" and i[5::].rstrip()==self.change_cls_inf_name:
                            temp[temp.index(i)+4]="Stor "+change_stor+'\n'
                file.close()
                file=open('Classes available',mode='w+')
                for items in temp:
                    file.write(items)
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
                System.UserName=get_username
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
            file=open('Classes available',mode="r")
            temp=file.readlines()
            temp2=[]
            for items in temp:
                if items[:4:]=="Name":
                    temp2.append(items[5::].rstrip())
            self.cls_search_name=input("输入你想查询的课程的名字:")
            if self.cls_search_name not in temp2:
                print("无此课程")
                return False
            for items in temp:
                if items[:4:]=="Name" and items[5::].rstrip()==self.cls_search_name:
                    print('课程名字:',items[5::].rstrip())
                    print('课程老师:',temp[temp.index(items)+1][5::].rstrip())
                    print('课程学分:',temp[temp.index(items)+2][5::].rstrip())
                    print('课程是否必修:',temp[temp.index(items)+3][5::].rstrip())
                    print('课程容量:',temp[temp.index(items)+4][5::].rstrip())
            file.close()
        else:
            print("请先登录")
            return False
try:
    system=System()
    system.Login()
    system.Change_cls()
except:
    Error=Exception("傻子用户又乱搞")
    raise Error

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
