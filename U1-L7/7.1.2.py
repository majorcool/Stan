'''def count():
    count+=1
    怎么限制递归次数啊啊啊
'''
a=0
def hahanum(n):
    global a
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
    if a==994:
        print("不是哈哈数")
        return False
    a+=1
    return hahanum(sum)
hahanum(20)
