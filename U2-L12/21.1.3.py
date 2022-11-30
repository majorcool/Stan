file=open('1.txt',mode='r')
a=file.read()
a=a.split('\n')
temp=[]
for items in a:
    if items[0]=='#':
        continue
    temp.append(items)
print(temp)
file.close()