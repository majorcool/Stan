i = 1
Num = int(input("请输入正整数"))
PanDing = 0
CiShu = 0
YesorNo = False
Two = 0
Three = 0
Five = 0
Seven = 0
Count = 0
Sum = 1
output = ""
Count2 = 0
Count3 = 0
Count5 = 0
CountSev = 0
TF = False
while i < Num:
    PanDing = Num % i
    if PanDing == 0:
        CiShu += 1
    if CiShu > 1:
        YesorNo = True
        break
    i += 1
if CiShu <= 1:
    print("是质数,无法分解")
    YesorNo = False
if YesorNo == True:
    while (1):
        if Num % 2 == 0:
            Num = Num / 2
            Count2 += 1
        else:
            break
    while (1):
        if Num % 3 == 0:
            Num = Num / 3
            Count3 += 1
        else:
            break
    while (1):
        if Num % 5 == 0:
            Num = Num / 5
            Count5 += 1
        else:
            break
    while (1):
        if Num % 7 == 0:
            Num = Num / 7
            CountSev += 1
        else:
            break
if YesorNo == True:
    print("分解公因式需要%d个2\n%d个3\n%d个5\n%d个7" % (Count2, Count3, Count5, CountSev))

