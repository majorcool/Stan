grade=0
sum=0
ave=0
for i in range (0,30):
    grade=int(input("请输入成绩:"))
    sum=sum+grade
ave=sum/30
print("平均分为: %f" % ave)