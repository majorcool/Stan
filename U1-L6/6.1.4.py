def delete(one,two):
    temp=[]
    for i in range (0,len(two)):
        temp.append(one[i])
    count=0
    while count<len(two):
        if temp[count] in one:
            one=one.replace(temp[count],"")
        else:
            count+=1
    print(one)
delete("abssjhsadhasdbasd","abss")