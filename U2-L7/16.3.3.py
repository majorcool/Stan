def repeat(n):
    c1=-1
    for items in n:
        if c1<n.count(items):
            c1=items
    return c1
print(repeat([5,1,5,2,5,3,5,4]))
