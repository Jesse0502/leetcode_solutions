"""
given an array of numbers there are two numbers that sum up to the target

loop through the numbers and store them in a hashmap, the target number should be a 
difference of target and some value that's already in the hashmap if it's found return the 
array [number found with difference, curr value in loop] 
"""


def twoSum(nums: list, target):
    prevMap = {}
    for i, n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[n] = i


print(twoSum([3, 2, 3], 5))
