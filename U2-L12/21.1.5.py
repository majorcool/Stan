file=open('3.txt',mode='r+')
file_new=open('3-new.txt',mode="r+")
find="abcdefghijklmnopqrstuvwxyz"
find2="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
file2=file.read()
for item in file2:
    if item in find:
        z=find.index(item)-1
        if z==-1:
            z=25
        file_new.write(find[z])
    elif item in find2:
        file_new.write(find2[find2.index(item)+1])
    else:
        file_new.write(file2[file2.index(item)])
file.close()
file_new.close()

