sum=0
for i in range(1,1001):
    for z in range (1,i-1):
        if i%z==0:
            sum=sum+z
    if sum==i:
        print(i)
    sum=0


