i=1
Num=int(input("请输入正整数"))
PanDing=0
CiShu=0
while i<Num:
    PanDing=Num%i
    if PanDing==0:
        CiShu+=1
    if CiShu>1:
        print("不是质数")
        break
    i+=1

if CiShu<=1:
    print("是质数")
