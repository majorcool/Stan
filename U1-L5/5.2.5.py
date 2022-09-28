#第一题
box=[[],[],[],[],[],[]]
count=1
for i in range(0,6):
    for z in range (0,6):
        box[i].append(count)
        count=count+1
print(box)
#第二题
count=1
count2=1
rol=[[],[],[],[],[],[]]#行
col=[[],[],[],[],[],[]]#列
for i in range(0,6):
    for z in range(0,6):
        rol[i].append(count)
        count=count+1
rol=tuple(rol)
for i in range (0,6):
    a=rol[i]
    for z in range(0,6):
        print(a[z],"\t",end="")
    print("")
count=0
for i in range(0,6):
    count2=i+1
    for z in range(0,6):
        col[i].append(count2)
        count2=count2+6
count=0
col=tuple(col)
for q in range (0,6):
    for z in range(0,6):
        a = col[z]
        for p in range (0,1):
              print(a[count],"\t",end="")
    print("")
    count = count + 1
#第三题
rol_sum=[]
col_sum=[]
sum=0
for i in range (0,6):
    sum=0
    a=rol[i]
    for l in range (0,6):
        sum=sum+a[l]
    rol_sum.append(sum)
print(rol_sum)

for i in range(0,6):
    sum=0
    a=col[i]
    for l in range (0,6):
        sum=sum+a[l]
    col_sum.append(sum)
print(col_sum)





