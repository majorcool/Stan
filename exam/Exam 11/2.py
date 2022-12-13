def small_array(l):
    max_edge=0
    biggest_num=0
    for item in l:
        if l.count(item)>max_edge:
            biggest_num=item
    min_st=l.index(biggest_num)
    max_end=[]
    for i,items in enumerate(l):
        if items==biggest_num:
            max_end.append(i)
    print(max(max_end)+1-min_st)
    return max(max_end)+1-min_st
with open('2.txt',mode='r') as f:
    file=f.readlines()
    for lines in file:
        strs=[]
        w=lines.split()[0]
        w=w.split(',')
        for items in w:
            strs.append(items)
            print(strs)
        ans=lines.split()[1]
        if small_array(strs)!=ans:
            print(False)