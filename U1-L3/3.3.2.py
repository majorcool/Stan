h=int(input("输入行数"))
Odd=True
if h%2==0:
    print("行数必须是奇数!!!")
    Odd=False

if Odd==True:
    for i in range(1,h//2+2):
        print(" "*(h-i),end="")
        print("*"*(2*i-1))
    for i in range(h//2,0,-1):
        print(" "*(h-i),end="")
        print("*"*(2*i-1))