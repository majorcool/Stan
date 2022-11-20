def two_list(l,n):
    l1=[]
    for i in range(n):
        l1.append(l[i])
        l1.append(l[i+n])
    print(l1)
two_list([1,2,3,4,4,3,2,1],4)
