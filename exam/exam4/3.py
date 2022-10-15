def reverse(n,str='123456789'):
    count=len(str)//n+1
    temp=[]
    temp.append(str[n-1::-1])
    for i in range(1,count+1):
        temp.append(str[(n*i)-1:(n*(i-1))-1:-1])
    for choice in temp:
        print(choice,end="")

reverse(2)
