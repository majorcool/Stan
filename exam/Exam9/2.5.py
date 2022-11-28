def min_cup(cups):
    count=0
    while 1:
        M_x=max(cups)
        M_n=min(cups)
        if M_x==0 and M_n==0:
            return count
        if M_n!=0:
            cups[cups.index(M_x)]-=1
            cups[cups.index(M_n)]-=1
        else:
            count+=M_x
            return count
        count+=1
print(min_cup([5,0,0]))