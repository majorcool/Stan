def LX(h):
    a=[]
    b=[]
    Odd = True
    if h % 2 == 0:
        print("行数必须是奇数!!!")
        Odd = False

    if Odd == True:
        for i in range(1, h // 2 + 2):
            a.append(" " * (h - i))
            a.append("*" * (2 * i - 1))
        for i in range(h // 2, 0, -1):
            a.append(" " * (h - i))
            a.append("*" * (2 * i - 1))
    return(a)
for i in range(0,len(LX(3))):
    print(LX(3)[i],end="")
