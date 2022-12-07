def rev_same(s):
    temp = str()
    s = s.split()
    Rev = []
    rev_s = ''
    temp3=str()
    for items in s:
        temp+=items
    temp=' '.join(temp)
    temp=temp.split()
    temp2=temp.copy()
    for i in range(0, len(temp)):
        Rev.append(temp.pop())
    for items in Rev:
        rev_s += items
    for items in temp2:
        temp3+=items
    if temp3 == rev_s:
        return True
    else:
        return False
print(rev_same('Iia L aiI'))