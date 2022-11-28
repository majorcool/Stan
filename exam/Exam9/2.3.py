def Top(gain):
    num=0
    record=[0]
    for items in gain:
        num+=items
        record.append(num)
    return max(record)
print(Top([-4,-3,-2,-1,4,3,2]))