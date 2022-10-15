def sum(num1,num2):
    count1=0
    count2=0
    if type(num1)==int and type(num2)==float:
        '''
         if str(num1)[0]=="-":
             count1+=1
         if str(num2)[0]=="-":
             count2+=1
         if type(num1)==int and type(num2)==float:
             num=num2//1
             num2=str(num2)
             if count2==1:
                 num2.replace("-","")
         '''
        num=num2//1
        num2=str(num2)
        num2=num2.split(".")
        sum_temp=num+num1
        sum_temp=int(sum_temp)
        '''
        if count1 == 1 and count2 == 1:
            print(sum_temp, ".", num1[1], sep="")
        elif count1==0 and count2==0:
            print(sum_temp, ".", num1[1], sep="")
        else:
            print("-",sum_temp, ".", num1[1], sep="")
        '''
        print(sum_temp,".",num2[1],sep="")
    if type(num1) == float and type(num2) == int:
        num = num1 // 1
        num1 = str(num1)
        num1 = num1.split(".")
        sum_temp = num + num2
        sum_temp = int(sum_temp)
        '''
           if count2==1:
               num2_str.replace("-","")
           if count1==1:
               num1_str.replace("-","")
           '''
        '''
         if count1 == 1 and count2 == 1:
             print(sum_temp,".",sum_temp2,sep="")
         elif count1==0 and count2==0:
             print(sum_temp,".",sum_temp2,sep="")
         else:
             print("-",sum_temp, ".", sum_temp2, sep="")
         '''
        print(sum_temp, ".", num1[1], sep="")
    if type(num1) == float and type(num2) == float:
        num1_int = int(num1//1)
        num2_int=int(num2//1)
        sum_temp=num1_int+num2_int
        num1_str=str(num1)
        num2_str=str(num2)
        num1_N=int(num1_str[2::])
        num2_N=int(num2_str[2::])
        sum_temp2=num1_N+num2_N
        print(sum_temp,".",sum_temp2,sep="")

sum(2.1111111111111,2.2222222222)