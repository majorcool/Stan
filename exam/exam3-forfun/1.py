def sum0(num_list):
    num_list=list(num_list)
    temp_list=()
    temp_list2=[]
    count=0
    for i in range(0,len(num_list)):
        temp_list2.append(" ")
    for i in range (0,len(num_list)):
        for o in range (0,len(num_list)):
            for p in range (0,len(num_list)):
                if num_list[i]+num_list[o]+num_list[p]==0:
                    temp_list=(num_list[i],num_list[o],num_list[p])
                    temp_list2[i]=temp_list
    print(set(temp_list2))#转换成数组后自动去处重复项
sum0([1,2,3,4,5,-1,-2,-3,-4,-5])




