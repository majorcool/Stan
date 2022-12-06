def plant(pos,n):
    continue_0=0
    can_plant=0
    for items in pos:
        if items==0:
            continue_0+=1
        if items==1:
            if continue_0>=3:
                continue_0-=1
                can_plant+=continue_0//2
            continue_0=0
    if pos[0]==0 and pos[1]==0:
        n-=1
    if pos[-1]==0 and pos[-2]==0:
        n-=1
    if can_plant>=n:
        return True
    else:
        return False
print(plant([0,0,1,0,0],n=1))
