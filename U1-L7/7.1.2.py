'''def count():
    count+=1
    怎么限制递归次数啊啊啊
'''
def hahanum(n):
    n=str(n)
    temp=[]
    sum=0
    for char in n:
        temp.append(int(char))
    for items in range(0,len(temp)):
        if items==0:
            continue
        temp[items]**=2
        sum+=temp[items]
    if sum==1:
        print("是蛤蛤数")
        return True
    return hahanum(sum)
hahanum(19)
