def climb_price(stairs):
    step = -1
    cost = 0
    while 1:
        if step+3>len(stairs):
            return cost
        if len(stairs)-2==step+1:
            if stairs[-2]>stairs[-1]:
                return cost+stairs[-2]
            else:
                return cost+stairs[-1]
        if step+4<=len(stairs):
            if stairs[step+1]+stairs[step+3]>stairs[step+2]:
                cost+=stairs[step]
                step+=2
            else:
                cost+=stairs[step+1]+stairs[step+3]
                step+=3
print(climb_price([1,4,4,80,2]))