class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        nums.sort()
        return nums[len(nums) - k]
    
print(   
Solution.findKthLargest(0,[3,2,3,1,2,4,5,5,6], 6)
)