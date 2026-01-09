def twoSum(nums, target):
    n = len(nums)
    print(n)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
nums=[1,12,13,15,7]
print(twoSum(nums,8))