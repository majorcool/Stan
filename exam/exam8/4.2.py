def pos_neg(list):
    Judge=0
    for items in list:
        if items==0:
            return 0
        if items<0:
            Judge+=1
    if Judge%2!=0:
        return -1
    else:
        return 1
print(pos_neg([-1,1,-1,1,-1]))