i=1
b=1
Num=int(input("请输入正整数,请勿输入质数"))
PanDing=0
Num1=Num
print("%d=" % Num,end="")
for i in range(1,Num):
    PanDing=Num%b
    if PanDing==0 and b!=1 and b!=Num1:
        print(b,end="")
        Num=Num/b
        if Num != 1:
            print("*",end="")
        continue
    b=b+1