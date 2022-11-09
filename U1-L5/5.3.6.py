def compare_dict(dict1,dict2):
    a=[]

    for key,value in dict1.items():
        for key2,value2 in dict2.items():
            if key==key2 and value==value2:
                a.append(str(key) +':'+str(value))
    a=tuple(a)
    return a
dict1={
    '1':5,
    '2':7,
    '3':4
}
dict2={
    '1':5,
    '2':7,
    '3':5
}
print(compare_dict(dict1,dict2))
