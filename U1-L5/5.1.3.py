pos_3=0
list_num=[1,3,4,3,7,3,9,8,6,3]
def num3():
    pos_3 = list_num.index(3)
    list_num.remove(3)
    return pos_3
a=0
for i in range(0,list_num.count(3)):
    a=num3()
    print(a+i)
print(list_num)





