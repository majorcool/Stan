def sub(a,b):
    if len(a)>len(b):
        long=a
        short=b
    else:
        long=b
        short=a
    if short in long:
        return -1
    temp=[]
    for items in short:
        temp.append(items)
    for item in long:
        temp.append(item)
    long_special='_'.join(long)
    short_special='_'.join(short)
    long_special=long_special.split('_')
    short_special=short_special.split("_")
    long_special=set(long_special)
    long_special=list(long_special)
    l_s=''
    s_s=''
    for items in long_special:
        l_s+=items
    for items in short_special:
        s_s+=items
    if l_s in s_s:
        return len(long)
    if len(set(temp))==len(long)-len(short):
        return -1
    else:
        return len(long)
print(sub('bubisyedstnyhqglexpcswbngwdyxyvgyhlwlnxpgisxvzywwimomwbzjbxjuzwnjuesea','qfmfvymoqputjgzdfepeazdjvewbftqdxvxgueztmdmkgp'))