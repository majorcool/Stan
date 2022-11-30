file=open('4.txt',mode='r+')
a=file.read()
count=0
print(a)
for item in a:
    if item.isupper()==True:
        file.seek(count)
        file.write(item.lower())
    if item.islower()==True:
        file.seek(count)
        file.write(item.upper())
    count+=1
file.close()