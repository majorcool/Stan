def unique(nums):
    str_nums=''
    for items in nums:
        str_nums+=str(items)
    for items in nums:
        if str_nums.count(str(items))>=2:
            str_nums=str_nums.replace(str(items),"")
    str_nums='o'.join(str_nums)
    str_nums=str_nums.split('o')
    if str_nums==['']:
        return 0
    sum=0
    for items in str_nums:
        sum+=int(items)
    return sum
print(unique([1,2,3,4,5]))