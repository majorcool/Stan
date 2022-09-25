def CFB(lieshu):
    TiaoMu=0
    for i in range(1, lieshu + 1, 1):
        TiaoMu=TiaoMu+i
    return TiaoMu
Lie=int(input("输入列数"))
Lie_Shu=CFB(Lie)
Sum=Lie_Shu
for i in range(0, Sum):
    if i>=1 and Lie_Shu>0:
        print("%d*%d=%d" % (1, i, i), end=" ")
        Lie_Shu=Lie_Shu-1
    if i >= 2 and Lie_Shu>0:
        print("%d*%d=%d" % (2, i, 2 * i), end=" ")
        Lie_Shu=Lie_Shu-1
    if i >= 3 and Lie_Shu>0:
        print("%d*%d=%d" % (3, i, 3 * i), end=" ")
        Lie_Shu = Lie_Shu - 1
    if i >= 4 and Lie_Shu>0:
        print("%d*%d=%d" % (4, i, 4 * i), end=" ")
        Lie_Shu = Lie_Shu - 1
    if i >= 5 and Lie_Shu>0:
        print("%d*%d=%d" % (5, i, 5 * i), end=" ")
        Lie_Shu = Lie_Shu - 1
    if i >= 6 and Lie_Shu>0:
        print("%d*%d=%d" % (6, i, 6 * i), end=" ")
        Lie_Shu = Lie_Shu - 1
    if i >= 7 and Lie_Shu>0:
        print("%d*%d=%d" % (7, i, 7 * i), end=" ")
        Lie_Shu = Lie_Shu - 1
    if i >= 8 and Lie_Shu>0:
        print("%d*%d=%d" % (8, i, 8 * i), end=" ")
        Lie_Shu = Lie_Shu - 1
    if i >= 9 and Lie_Shu>0:
        print("%d*%d=%d" % (9, i, 9 * i), end=" ")
        Lie_Shu = Lie_Shu - 1
    print("")
print("条目=%d" % Sum)