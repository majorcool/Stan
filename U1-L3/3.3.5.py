'''import random
l=[]
for i in range(0,24):
    first=""
    second=""
    a=random.choice(["1","2","3","4"])
    b=random.choice(["1","2","3","4"])
    c=random.choice(["1","2","3","4"])
    d=random.choice(["1","2","3","4"])
    while(1):
        if a==b or a==c or a==d or b==c or b==d or c==d:
            a = random.choice(["1", "2", "3", "4"])
            b = random.choice(["1", "2", "3", "4"])
            c = random.choice(["1", "2", "3", "4"])
            d = random.choice(["1", "2", "3", "4"])
        else:
            break
    if i==1:
         while second==first or a == b or a == c or a == d or b == c or b == d or c == d:
             a = random.choice(["1", "2", "3", "4"])
             b = random.choice(["1", "2", "3", "4"])
             c = random.choice(["1", "2", "3", "4"])
             d = random.choice(["1", "2", "3", "4"])
             second=a+b+c
    l.append=(a+b+c)
    if i==0:
        print(first)
    else:
        print(second)
'''
count=0
for num1 in range(1,5):
    for num2 in range (1,5):
        for num3 in range(1,5):
            if num1==num2 or num1==num3 or num2==num3:
                continue
            print(str(num1)+str(num2)+str(num3),end=' ')
            count+=1
print(',total:',count)