def reverse(n,str='123456789'):
    count=len(str)//n+1
    temp=[]
    for i in range(0,count):
        if i==0:
            temp.append(str[])
        else:
            temp.append(str[n*(i+1):n*i:-1])

    print(temp)

reverse(3)
