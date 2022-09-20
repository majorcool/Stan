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
print("1234,1243,1324,1342,1423,1432,2134,2143,2341,2314,2413,2431,3124,3142,3241,3214,3412,3421,4123,4132,4231,4213,4321,4312")