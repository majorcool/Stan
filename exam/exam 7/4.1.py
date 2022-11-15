def gcd_pro_max_1(* nums: int) -> int:
    if len(set(nums)) == 1:
        return set(nums).pop()
    nums = sorted(nums, reverse=True)
    # print(nums)
    for i in range(len(nums)-1):
        if nums[i] % nums[i+1] == 0:
            nums[i] = nums[i+1]
        else:
            nums[i] = nums[i] % nums[i+1]
    return gcd_pro_max_1(*nums)

def gcd_pro_max_2(* nums: int) -> int:
    nums = list(nums)
    while len(set(nums)) > 1:
        nums = sorted(nums)
        # print(nums)
        for i in range(len(nums)-1, 0, -1):
            if nums[i] % nums[i-1] == 0:
                nums[i] = nums[i-1]
            else:
                nums[i] = nums[i] % nums[i-1]
    return set(nums).pop()
print(gcd_pro_max_2(2,3,4,5))