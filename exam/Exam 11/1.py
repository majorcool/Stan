def common_prefix(strs):
    c_prefix=''
    result=''
    c_prefix=strs[0]
    for i in range(len(strs)):
        for char in c_prefix:
            if len(strs[i].removeprefix(c_prefix))==len(strs[i]):
                c_prefix=c_prefix.removesuffix(c_prefix[-1])
    return c_prefix
with open('1.txt',mode="r") as f:
    file=f.readlines()
    for lines in file:
        strs=[]
        w=lines.split()[0]
        w=w.split(',')
        for items in w:
            strs.append(items)
        ans=lines.split()[1]
        if common_prefix(strs)!=ans:
            print(False)

