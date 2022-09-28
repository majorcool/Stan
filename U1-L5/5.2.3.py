def ave(number):
    alldata=[]
    alldatas=(7,5)
    sum=0
    for i in range(0,number):
        score=float(input("输入学生成绩:"))
        while 1:
            if score>100 or score<0:
                score=float(input("数据错误，请重新输入"))
            else:
                break
        alldata.append(score)
    alldatas=tuple(alldata)
    return alldatas
a=ave(5)
sum=0
for i in range(0,len(a)):
    print(a[i],end="")
    print(" ",end="")
    sum=sum+a[i]
average=sum/len(a)
print("\n平均分为", average)
a=list(a)
a[1]=88
a=tuple(a)
sum=0
for i in range(0,len(a)):
    sum=sum+a[i]
average=sum/len(a)
print("经修改后的平均分为",average)

