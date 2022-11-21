def largest_perimeter(nums):
    nums.sort(reverse=True)
    print(nums)
    for x in range (0,len(nums)-2):
        y=x+1
        z=y+1
        if nums[y]+nums[z]>nums[x]:
            print(x,y,z)
            return nums[x]+nums[y]+nums[z]
    return 0
print(largest_perimeter([1,2,2,4,2]))