i = 1
Num = int(input("请输入正整数"))
YesorNo = 0
count = 0
while i < Num:
    YesorNo = Num % i
    if YesorNo == 0:
        count += 1
    if count > 1:
        print("不是质数")
        break
    i += 1

if count <= 1:
    print("是质数")


