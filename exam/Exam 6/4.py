def max_sec_average(l,n):
    count=len(l)-n
    sum=0
    final=0
    for i in range (0,count):
        for z in range(i,i+n):
            sum+=l[z]
        if final<sum:
            final=sum
        sum=0
    print(final/n)
max_sec_average([1,12,-5,-6,50,3],4)
