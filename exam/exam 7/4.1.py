maxvalue=1
def promax(n):
    n.sort()
    for items in n:
        for o in range (0,len(n)-1):
            n.sort()
        for i in range(1,len(n)):
            if n[o]%n[i]==0:
                n[o]=n[i]
            else:
                n[o]=n[o]%n[i]
    print(max(n))
def promaxv2(n):
    global maxvalue
    for items in n:
        if items % max!=0:
            return(promaxv2(n))
    if max==max(n):
        return max
    else:
        maxvalue+=1
        return (promaxv2(n))
promax([27,9,102])


