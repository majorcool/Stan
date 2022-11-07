def reverse_vowels(s):
    change=['a','e','i','o','u','A','E','I','O','U']
    temp=[]
    for char in s:
        if char in change:
            temp.append(char)
    temp.reverse()
    s='_djiwedhiuedhiwehd%^*%0129dj'.join(s)
    s=s.split('_djiwedhiuedhiwehd%^*%0129dj')
    count=-1
    count2=0
    temp2=temp
    for i in range(len(s)-1,-1,-1):
        if s[i] == temp2[count2]:
            s[i]=temp[count]
            count-=1
            count2+=1
            if count2==len(temp2):
                for char in s:
                    print(char, end='')
                return False
    for char in s:
        print(char,end='')
reverse_vowels('CoopEdu2022')