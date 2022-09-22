m=int(input("输入正整数m"))
n=int(input("输入正整数n"))
sum=0
k=0
for i in range(0,n):
    k=k+1
    for i in range(0,k):
       sum = sum + m * (10 ** i)
print(sum)