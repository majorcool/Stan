def CFB(lieshu):
    TiaoMu=0
    for i in range(1, lieshu + 1, 1):
        TiaoMu=TiaoMu+i
    return TiaoMu
Lie=int(input("输入列数"))
Lie_Shu=CFB(Lie)
Sum=Lie_Shu
for i in range(1, Lie+1):
    for p in range (1,i+1):
        print(i,"*",p,"=",i*p,end=" ")
    print("")
print("条目=%d" % Sum)