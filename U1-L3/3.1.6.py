Score=0
Sum=0
Ave=0
i=0
while i<30:
    Score=int(input("分数:"))
    if Score>100 or Score<0:
        print("分数有误请重新输入")
        continue
    Sum=Sum+Score
    i+=1

Ave=Sum/30
print("平均分为%.2f" % Ave)