maxvalue=1
mv=0
def promax(n):
    n.sort(reverse=True)
    count=0
    while max(n)!=min(n):
        count+=1
        for o in range(0,len(n)-1):
           a=o+1
           if n[o]%n[a]==0:
               n[o]=n[a]
           else:
               n[o]=n[o]%n[a]
        if count>=994:
            print("1")
            return False
    print(max(n))
def promaxv2(n):
    global maxvalue,mv
    for items in n:
        if items % maxvalue!=0:
            maxvalue+=1
            return(promaxv2(n))
    mv+=1
    if maxvalue==max(n):
        return mv
    else:
        maxvalue+=1
        return (promaxv2(n))
promaxv2([2, 4, 6, 8, 10])


