while True:
    a = int(input("请输入一个正整数，不能是质数"))
    for i in range(1,a+1):
        if a%i==0:
            print(i)
    continue