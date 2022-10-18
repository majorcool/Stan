def trans(num):
    temp=[]
    stri=""
    roman=[1,4,5,9,10,40,50,90,100,400,500,900,1000]
    for i in range (len(roman)-1,-1,-1):
        while 1:
            if num//roman[i]>0:
                temp.append(roman[i])
                num-=roman[i]
            else:
                break
    for item in temp:
        if item==1:
            temp[temp.index(item)]="I"
        if item==4:
            temp[temp.index(item)]="IV"
        if item==5:
            temp[temp.index(item)]="V"
        if item==9:
            temp[temp.index(item)]="IX"
        if item==10:
            temp[temp.index(item)]="X"
        if item==40:
            temp[temp.index(item)]="XL"
        if item==50:
            temp[temp.index(item)]="L"
        if item==90:
            temp[temp.index(item)]="XC"
        if item==100:
            temp[temp.index(item)]="C"
        if item==400:
            temp[temp.index(item)]="CD"
        if item==500:
            temp[temp.index(item)]="D"
        if item==900:
            temp[temp.index(item)]="CM"
        if item==1000:
            temp[temp.index(item)]="M"
    for str in temp:
        stri+=str
    print(stri)
trans(2001)
