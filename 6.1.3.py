def reverse(str_):
    temp=[]
    temp_str=str()
    for char in str_:
        temp.append(char)
    for i in range(len(temp)-1,-1,-1):
        temp_str+=temp[i]
    return temp_str
print(reverse('abc'))