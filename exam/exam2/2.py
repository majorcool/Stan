while(1):
    Num1=float(input("输入数字一"))
    Num2=float(input("输入数字二"))
    YunSuanFangFa=int(input("选择运算方法:1.加2.减3.乘4.除"))
    Chu=0
    Cheng=0
    if YunSuanFangFa==1:
        print(Num1+Num2)
    elif YunSuanFangFa==2:
        print(Num1-Num2)
    elif YunSuanFangFa==3:
        Cheng=Num1*Num2
        print("%f" % Cheng)
    else:
        Chu=Num1/Num2
        print("%f" % Chu)