def MissingNumber(nums):
    output = 0
    for i, n in enumerate(nums):
        if not i in nums:
            output = i
        if not len(nums) in nums:
            output = len(nums)
    print(output)
    return output            

MissingNumber([1,2,5,4,0])