a=[1,2,3,4,5]
def sep():
    b=len(a)
    c=1
    if b%2==0:
        b=b-1
        while b>0:
            a.insert(c,0)
            c=c+2
            b=b-1
    else:
        b=b-1
        while b>0:
            a.insert(c,0)
            c=c+2
            b=b-1
    return a
print(sep())
