"""
Take two pointers, keep first one the first index of numbers and other on the last.
while elem at j is greater than i check the sum of numbers[i] + numbers[j] == target
if true then return [j+1, i+1] elif sum is greater than target then j index -1 otherwise i+1
"""

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers)-1
        while i < j:
            if numbers[i]+numbers[j] == target:
                return [i+1, j+1]
            elif numbers[i]+numbers[j] > target:
                j -= 1
            else:
                i += 1
