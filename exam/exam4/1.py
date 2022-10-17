def pattern(x,list_input=[],direction='right'):
    if direction!= 'right' and direction!='left':
        print("direction只能是left或者right")
        return False
    if direction=='right':
        print(list_input[x+1::]+list_input[:x+1:])
    if direction=='left':
        print(list_input[x::]+list_input[:x:])
pattern(2,[1,2,3,4,5],'left')
