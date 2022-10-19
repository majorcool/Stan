def findlist(num):
    count=1
    temp_str=''
    alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    while 1:
        if num//26**count>1:
            count+=1
        else:break
    if count>1:
        count-=1
    for i in range (count,-1,-1):
        temp_str+=alphabet[num//(26**i)-1]
        div=num//(26**i)
        num=num-div*(26**i)
    print(temp_str)
findlist(2147483647)