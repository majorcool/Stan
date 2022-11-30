file=open('bad boy.txt', mode="r+")
a=file.readlines()
pointer=0
temp=''
for items in a:
    space=items.count(' ')
    if space%4!=0:
        space=4-(space%4)
        temp+=" "*space
        temp+=items
        file.seek(pointer)
        file.write(temp)
    pointer+=len(items)
for items in a:
    print(items)
file.close()
#尽力啦，不会写