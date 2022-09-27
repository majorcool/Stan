pos_3=0
list_num=[1,3,4,3,7,3,9,8,6,3]
def num3():
    pos_3 = list_num.index(3)
    list_num.remove(3)
    print(pos_3)
for i in range(0,list_num.count(3)):
    num3()
print(list_num)





