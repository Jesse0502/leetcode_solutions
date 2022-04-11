def findDisappearedNumbers(nums):
    output = []
    
    for i in (range(1, len(nums) + 1)):
        if not i in nums:
            output.append(i)
            
    return output


print(findDisappearedNumbers([1,6,2,4]))