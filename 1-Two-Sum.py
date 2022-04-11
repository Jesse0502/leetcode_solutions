def twoSum(nums: list, target):
    prevMap = {}
    for i, n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[n] = i
    print(nums,target)

print(twoSum([3,2,3], 5))