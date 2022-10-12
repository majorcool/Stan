def judge(str_temp):
    temp="o".join(str_temp)
    count=temp.count("o")
    count+=1
    judgement=str()
    judgement2=str()
    mid=int(count//2)
    if count%2!=0:
        mid-=1
        compare1=int(str_temp[mid+1])
        compare2=int(str_temp[mid])
        if compare2+1==compare1:
            str_temp2=str_temp.split(str_temp[mid+1])
            judgement=str_temp2[0]
            judgement2=str_temp2[1]
            judgement='0'.join(judgement)
            judgement2='0'.join(judgement2)
            judgement=judgement.split('0')
            judgement2=judgement2.split('0')
            judgement3=[]
            for i in range(len(judgement)-1,-1,-1):
                judgement3.append(judgement[i])
            for i in range(0,len(judgement)):
                if judgement3[i]!=judgement2[i]:
                    print("不是回文数")
                    return False
            print("是回文数")

        else:
            print("不是回文数")
    str_temp.strip("o")
    if count%2==0:
        for i in range (0, count):
            if i<mid:
                judgement+=str_temp[i]
            if i>=mid:
                judgement2+=str_temp[(count-1+int(count/2))-i]
        if judgement==judgement2 and int(judgement[mid-2])+1==int(judgement[mid-1]):
            print("是回文数")
        else:
            print("不是回文数")
judge("1234554321")
