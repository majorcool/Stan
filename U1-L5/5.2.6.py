integer=[1,2,5,3,2,3]
integer.sort()
a=0
b=0
while len(integer)>1:
    a=integer[0]
    integer.pop(0)
    b=integer[0]
    integer.pop(0)
    integer.append(a*b-1)
    integer.sort()
print(integer[0])