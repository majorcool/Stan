def triangle(a,b,c):
    l=[a,b,c]
    l.sort(reverse=True)
    if l[0]>=l[1]+l[2]:
        IllegalArguementException=Exception("a,b,c不能构成三角形")
        raise IllegalArguementException
    return l
print(triangle(1,2,2))