def score():
    Score=[]
    for i in range(0,7):
        while 1:
            a=float(input("输入成绩"))
            if a<0 or a>10:
                print("请输入正确的成绩")
            else:
                break
        Score.append(a)
    Hard=float(input("请输入难度系数"))
    Score.sort()
    Score.pop(0)
    Score.pop(0)
    Score.pop()
    Score.pop()
    Sum=Score[0]+Score[1]+Score[2]
    Final_score=Sum*Hard
    return Final_score
a=score()
print("最终成绩是%.2f" % a)

