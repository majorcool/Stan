def Dis(x,y):
    x1=[]
    y1=[]
    x=bin(x)
    y=bin(y)
    x=x.lstrip('0b')
    y=y.lstrip('0b')
    x='o'.join(x)
    x=x.split("o")
    y='o'.join(y)
    y=y.split("o")
    if len(x)<len(y):
        for i in range(len(y)-len(x)):
            x1.append(0)
        x1.extend(x)
        x=x1
    if len(y)<len(x):
        for i in range(len(x)-len(y)):
            y1.append(0)
        y1.extend(x)
        y=y1
    temp=set(x).intersection(set(y))
    print(len(x)-len(temp))
Dis(3,1)



