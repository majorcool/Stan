def connect(a,b):
    temp=""
    for i in b:
        temp+=i
    temp2=a.join(temp)
    return temp2
print(connect("aaa",["l","z","s"]))

#可以用join方法
