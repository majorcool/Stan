def sum0(num_list):
    result=[]
    for i in range (0,len(num_list)-2):
        for o in range (i+1,len(num_list)-1):
            for p in range (o+1,len(num_list)):
                x,y,z=num_list[i],num_list[o],num_list[p]
                if x+y+z==0:
                    result.append(tuple(sorted((x,y,z))))
    return list(set(result))
print(sum0([1,1,2,3,4,5,-1,-2,-3,-4,-5]))




