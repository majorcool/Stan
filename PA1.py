Pos=[1,2,3,4,5,6,7,8,9]
Map_line1=[" "," | "," "," | "," "]
Map_line2=[" "," | "," "," | "," "]
Map_line3=[" "," | "," "," | "," "]
Repeat=[0,0,0,0,0,0,0,0,0]
win_list=[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
judgep1=[]
judgep2=[]
win=False
def map():#打印每次的地图
    for i in range(0,5):
        print(Map_line1[i],end="")
    print("\n---------")
    for i in range(0, 5):
        print(Map_line2[i],end="")
    print("\n---------")
    for i in range(0, 5):
        print(Map_line3[i],end="")
def p1():#玩家1下棋
    while 1:
        player1 = int(input("输入想要下棋的位置:(1-9)"))
        if player1<1 or player1>9 or Repeat[player1-1]==1:
            print("请重新输入")
        else:
            break
    if player1>=1 and player1<=3:
        Map_line1[(player1-1)*2]="x"
    if player1>3 and player1<=6:
        Map_line2[(player1-4)*2]="x"
    if player1>6 and player1<=9:
        Map_line3[(player1-7)*2]="x"
    judgep1.append(player1)
    Repeat[player1-1]=1
def p2():#玩家2下棋
    while 1:
        player2 = int(input("输入想要下棋的位置:(1-9)"))
        if player2<1 or player2>9 or Repeat[player2-1]==1:
            print("请重新输入")
        else:
            break
    if player2>=1 and player2<=3:
        Map_line1[(player2-1)*2]="o"
    if player2>3 and player2<=6:
        Map_line2[(player2-4)*2]="o"
    if player2>6 and player2<=9:
        Map_line3[(player2-7)*2]="o"
    judgep2.append(player2)
    Repeat[player2-1]=1
def judge1():#判断玩家1输赢
    for i in range(0,8):
        temp_list=j1.intersection(win_list[i])
        if sorted(temp_list)==win_list[i]:
            return True
def judge2():#判断玩家2输赢
    for i in range(0,8):
        temp_list2=j2.intersection(win_list[i])
        if sorted(temp_list2)==win_list[i]:
            return True
map()
count=0
while 1:
    count+=1
    j1 = set(judgep1)
    j2 = set(judgep2)
    if judge1()==True or judge2()==True:
        break
    p1()
    j1 = set(judgep1)
    map()
    judge1()
    if judge1()==True:
        print("P1wins")
        break
    if judge2()==True:
        print("P2wins")
        break
    p2()
    j2 = set(judgep2)
    if judge1()==True:
        print("P1wins")
        break
    if judge2()==True:
        print("P2wins")
        break
    map()
    judge2()
    if count==8:
        print("pingju")
        break



