def max_sec_average(l,n):
    count=len(l)-n
    sum=0
    ave=0
    for i in range (0,count):
        for z in range(i,i+n):
            sum+=l[z]
        if ave<sum/n:
            ave=sum/n
        sum=0
    print(ave)
max_sec_average([1,12,-5,-6,50,3],4)
