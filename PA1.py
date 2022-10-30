import os
import sys
Pos=[1,2,3,4,5,6,7,8,9]
Map_line1,Map_line2,Map_line3=["1"," | ","2"," | ","3"],["4"," | ","5"," | ","6"],["7"," | ","8"," | ","9"]
Repeat=[0,0,0,0,0,0,0,0,0]
Win_list=[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]#判断输赢用的列表，里面包含了所有的胜利方法，之所以要从小到大写是为了方便sort
judge_p1,judge_p2,list_del=[],[],[]
Count,Count1=0,0
Win=False
def Tpnum(temp_num): #用于填补被删掉的棋子
    if temp_num >= 1 and temp_num <= 3:
        Map_line1[(temp_num - 1) * 2] = str(temp_num)
    if temp_num > 3 and temp_num <= 6:
        Map_line2[(temp_num - 4) * 2] = str(temp_num)
    if temp_num > 6 and temp_num <= 9:
        Map_line3[(temp_num - 7) * 2] = str(temp_num)
def print_map():#打印每次的地图
    for i in range(0,5):
        print(Map_line1[i],end="")
    print("\n---------")
    for i in range(0, 5):
        print(Map_line2[i],end="")
    print("\n---------")
    for i in range(0, 5):
        print(Map_line3[i],end="")
def P1():#玩家1下棋
    while 1:
        Player1_type =input("输入想要下棋的位置:(1-9)")
        if Player1_type.isdigit()==False:#防止用户输入数字以外的字符导致程序崩溃
            print("请输入1-9之间的数字!!!!")
            continue#输错了就继续循环直到输对
        Player1=int(Player1_type)
        if Player1<1 or Player1>9 or Repeat[Player1-1]==1: #防止重复下棋或者下到棋盘外面
            print("请重新输入")
        else:
            break
    if Player1>=1 and Player1<=3:
        Map_line1[(Player1-1)*2]="x"
    if Player1>3 and Player1<=6:
        Map_line2[(Player1-4)*2]="x"#通过判断数字在第几行然后再下棋
    if Player1>6 and Player1<=9:
        Map_line3[(Player1-7)*2]="x"
    judge_p1.append(Player1)#记录下棋
    list_del.append(Player1)#记录下棋用于删除
    Repeat[Player1-1]=1
def P2():#玩家2下棋
    while 1:
        Player2_type = input("输入想要下棋的位置:(1-9)")
        if Player2_type.isdigit()==False:
            print("请输入1-9之间数字!!!!")
            continue
        Player2=int(Player2_type)
        if Player2<1 or Player2>9 or Repeat[Player2-1]==1:
            print("请重新输入")
        else:
            break
    if Player2>=1 and Player2<=3:
        Map_line1[(Player2-1)*2]="o"
    if Player2>3 and Player2<=6:
        Map_line2[(Player2-4)*2]="o"
    if Player2>6 and Player2<=9:
        Map_line3[(Player2-7)*2]="o"
    judge_p2.append(Player2)
    Repeat[Player2-1]=1
    list_del.append(Player2)
def judge_1():#判断玩家1输赢
    for i in range(0,8):
        temp_list=J1.intersection(Win_list[i])#取p1下过的位置和获胜列表的交集，如果交集包括获胜列表中的所有元素，那就获胜
        if sorted(temp_list)==Win_list[i]:
            return True
def judge_2():#判断玩家2输赢
    for i in range(0,8):
        temp_list2=J2.intersection(Win_list[i])
        if sorted(temp_list2)==Win_list[i]:
            return True
print_map()#刚开始先打印一遍棋盘（防傻瓜）
temp_num=0
def delete_chess():#用于进阶玩法的删除棋子
    global Count
    if Count == 6 and choose == '2':
        print(list_del[0], "号位置的棋子即将被删除")
    if Count == 7 and choose == '2':
        Count -= 1
        temp_num = list_del[0]
        Repeat[temp_num - 1] = 0
        print(list_del[0], "号位置的棋子已经被删除")
        list_del.pop(0)
        print(list_del[0], "号位置的棋子即将被删除")
        if temp_num in judge_p2:
            judge_p2.pop(0)
            Tpnum(temp_num)
        else:
            judge_p1.pop(0)
            Tpnum(temp_num)
while 1:
    choose=input("选择玩法:1.普通玩法2.高阶玩法,输入1或2:")#选择模式
    if choose!="1" and choose!="2":#防傻瓜
        print("请输入正确的玩法")
        continue
    Pos = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    Map_line1, Map_line2, Map_line3 = ["1", " | ", "2", " | ", "3"], ["4", " | ", "5", " | ", "6"], ["7", " | ", "8", " | ", "9"]
    Repeat = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    Win_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    judge_p1,judge_p2,list_del = [],[],[]
    Count,Count1 = 0,0
    Win = False#以上所有变量初始化一遍
    while 1:#循环中循环，不然break就退出程序了
        J1,J2 = set(judge_p1),set(judge_p2)#只有set能用intersection方法
        P1()
        Count+=1
        Count1+=1
        os.system('cls')#清空棋盘
        delete_chess()
        J1 = set(judge_p1)
        print_map()
        if judge_1()==True:#P1下完棋后要判断一次
            print("P1Wins")
            break
        if judge_2()==True:
            print("P2Wins")
            break
        if Repeat.count(1)==9:
            print("和局")
            break
        P2()
        Count+=1
        Count1+=1
        os.system('cls')#清空棋盘
        delete_chess()
        J2 = set(judge_p2)
        if judge_1()==True:#P2下完棋后要判断一次
            print("P1Wins")
            break
        if judge_2()==True:
            print("P2Wins")
            break
        if Repeat.count(1)==9:#在判定完P1P2胜负后再判断和局
            print("和局")
            break
        print_map()