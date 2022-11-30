file=open('2.txt',mode='r')
a=file.read()
find=[1,2,3,4,5,6,7,8,9,10]
for item in find:
    if str(item) in a:
        print(item)
file.close()