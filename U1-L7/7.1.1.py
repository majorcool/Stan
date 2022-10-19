def arrange(s1,s2):
    count=0
    for char in s1:
        if char in s2:
            count+=1
    if count==len(s2):
        return True
    else:
        return False
print(arrange("alss","assl"))