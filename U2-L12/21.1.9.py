file=open('1.txt',mode="r")
file_new=open('1-new2.txt',mode="w+")
a=file.readlines()
for items in a:
    file_new.write(items)
file.close()
file_new.close()