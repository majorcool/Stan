import random
a=input()
b=input()
c=random.randint(int(a),int(b))
if a.isdigit()!=True or b.isdigit()==False:
    er=Exception("不是整数")
    raise er
if a>b:
    ers=Exception("起点大于终点")
    raise ers
print(c)