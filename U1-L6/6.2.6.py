def findlist(num):
    count=1
    temp_str=''
    alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    fl=float()
    num2=num
    while 1:
        fl=num2/(26**count)
        if fl>1:
            num2-=26**count
            count+=1
        else:
            break
    if num<=26:
        print(alphabet[num-1])
        return False
    if count>1:
        count-=1
    for i in range (count,-1,-1):
        temp_str+=alphabet[num//(26**i)-1]
        div=num//(26**i)
        num=num-div*(26**i)
    print(temp_str)
findlist(1)