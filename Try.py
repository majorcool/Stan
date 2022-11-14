class Solution(object):
    def twoSum(self, nums, target):
        temp=[]
        for items in nums:
            for  item in nums:
                if nums.count(items)>=2:
                    if target//2==items:
                        print(nums.index(items,0,len(nums)-1))
                        print(nums.index(items,1,len(nums)-1))
                    if items +item==target:
                        temp.append(nums.index(items))
                        temp.append(nums.index(item))
                        return temp
a=Solution()
a.twoSum([3,3],6)