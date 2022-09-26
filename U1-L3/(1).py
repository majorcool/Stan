grade=0
sum=0
ave=0
i=0
while i<=30:
    if grade<0 or grade>100:
        print("请输入正确的值")
        continue
    grade = int(input("请输入成绩:"))
    sum = sum + grade
    i=i+1
ave=sum/30
print("平均分为: %f" % ave)