a=[1,2,3,4,5]
def twice():
    b=len(a)
    for i in range(0,b):
        a[i]*=2
    return a
print(twice())