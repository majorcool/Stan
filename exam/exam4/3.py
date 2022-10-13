def reverse(n,str='123456789'):
    count=len(str)//n+1
    temp=[]
    for i in range(1,count+1):
        temp.append(str[(n*i)-1:(n*(i-1))-1:-1])
    print(temp)

reverse(3)
