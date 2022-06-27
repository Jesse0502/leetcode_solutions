
"""
Convert the given list of nums in to set -> loop through all the nums. If num-1 is not found in set, then add 1 to count and add 1 to curr and use while to loop ahead until it's in the set increase the count by 1. If count is greater than the max length, then return the max length 

"""

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        setList = set(nums)
        maxLen = 1
        for num in setList:
            if not num-1 in setList:
                count = 1
                curr = num
                while curr+1 in setList:
                    count += 1
                    curr += 1
                if count > maxLen:
                    maxLen = count
        return maxLen


Solution.longestConsecutive(Solution, [0, 3, 7, 2, 5, 8, 4, 6, 0, 1])
