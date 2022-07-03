"""
Statement - Given a list of integers, we need to return total possible combinations of three different integers that sum up to 0.

Solution - Sort the list. Now loop through the list and for each element check if the index of current element is greater than 0 and the element itself is same as the last one -> curr == nums[i - 1]. If yes, then continue. If not, Solve the problem as twoSum where target is 0. If curr + nums[l] + nums[r] is less that 0 then increment left pointer and vice versa. If it sums up to zero then append the three integers to res list and increment the left pointer to 1 and inside a while loop increment l again if nums[l] == nums[l - 1] and l < r. Return the res list.
"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, curr in enumerate(nums):
            if i > 0 and curr == nums[i - 1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                three_sum = curr + nums[l] + nums[r]
                if three_sum == 0:
                    res.append([curr, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                elif three_sum > 0:
                    r -= 1
                else:
                    l += 1
        return res
