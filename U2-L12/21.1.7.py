import os
file=open('zmcxbvn.txt',mode='r+',encoding='utf-8')
name=file.name
a=file.readlines(1)
a=str(a[0])
a=a.rstrip('\n')
a+='.txt'
print(a)
file.close()
os.rename(name,a)
file.close()
