Num=89
guess=0
while(1):
    guess=int(input("输入1-100数字"))
    Sub= Num - guess
    if Sub<0:
        Sub=Sub*-1
    if guess==Num:
        print("猜对了")
        break
    if Sub>50:
        print("离谱")
        continue
    if Sub>30:
        print("nonono")
        continue
    if Sub>10:
        print("Kind of close")
        continue
    if Sub<=10:
        print("Close!")