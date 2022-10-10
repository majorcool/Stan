'''def compare_dict(dict1,dict2):
    a=[]
    repeat=0
    for key,value in dict1:
        for key2,value2 in dict2:
            if key==key2 and value==value2:
                repeat+=1
                a.append(key,value)
    a=tuple(a)
    print(repeat)
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
compare_dict(dict1,dict2)
'''