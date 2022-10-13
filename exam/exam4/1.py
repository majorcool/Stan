def pattern(x,list_input=[],direction='right'):
    temp=[]
    if direction!= 'right' and direction!='left':
        print("direction只能是left或者right")
        return False
    if direction=='right':
        lens=len(list_input)
        temp.append(list_input[-x:lens])
        temp.append(list_input[0:-x])
        temp[0].extend(temp[1])
        print(temp[0])
    if direction=='left':
        lens=len(list_input)
        temp.append(list_input[x:lens])
        temp.append(list_input[0:x])
        temp[0].extend(temp[1])
        print(temp[0])
pattern(2,[1,2,3,4,5],'left')
