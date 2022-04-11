def SingleNumber(nums):
    res = 0
    for n in nums:
        res = n ^ res
    return res

print(SingleNumber([1,1,2,2,4,4,5]))