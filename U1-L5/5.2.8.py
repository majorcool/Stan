def repeat():
    i=0
    z=1
    while i<=len(Sample):
        z=i+1
        while z<len(Sample):
            if Sample[i]==Sample[z]:
                Sample.pop(z)
            z+=1
        i+=1
Sample=[1,2,6,7,9,10,10,9,3,4,1,2,3,4]
repeat()
Sample=tuple(Sample)
print(sorted(Sample))
