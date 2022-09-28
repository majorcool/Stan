def ave(number):
    sum=0
    for i in range(0,number):
        score=float(input("输入学生成绩:"))
        while 1:
            if score>100 or score<0:
                score=float(input("数据错误，请重新输入"))
            else:
                break
        sum=sum+score
    return sum/number
print(ave(5))