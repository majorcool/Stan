def plus1(num):
    temp=0
    count=1
    temp1=[]
    for i in range(len(num)-1,-1,-1):
        temp+=num[i]*count
        count*=10
    temp+=1
    temp=str(temp)
    for char in temp:
        temp1.append(int(char))
    return temp1
print(plus1([9,9,9]))