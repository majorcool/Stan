def trans(num):
    temp=[]
    sum=0
    roman=["IV","IX","XL","XC","CD","CM"]
    roman2=["I","V","X","L","C","D","M"]
    for items in roman:
        if items in num:
            temp.append(items)
            num=num.replace(items,"")
    while num!="":
        for items in roman2:
            if items in num:
                for i in range (0,num.count(items)):
                    temp.append(items)
                num=num.replace(items,"")
    for item in temp:
        if item=="IV":
            sum+=4
        if item=="IX":
            sum+=9
        if item=="XL":
            sum+=40
        if item=="XC":
            sum+=90
        if item=="CD":
            sum+=400
        if item=="CM":
            sum+=900
        if item=="I":
            sum+=1
        if item=="V":
            sum+=5
        if item=="X":
            sum+=10
        if item=="L":
            sum+=50
        if item=="C":
            sum+=100
        if item=="D":
            sum+=500
        if item=="M":
            sum+=1000
    print(sum)
trans("MMMCMLXIII")
