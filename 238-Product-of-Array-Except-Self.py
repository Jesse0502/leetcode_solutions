from typing import List


class Solution:
    def productExceptSelf(self, nums):
        left_product = []

        left = 1
        for i in nums:
            left_product.append(left)
            left = left * i

        right_product = []
        right = 1
        for i in reversed(nums):
            right_product.append(right)
            right *= i
        output = []
        for l, r in zip(left_product, reversed(right_product)):
            output.append(l*r)
        return (output)


Solution.productExceptSelf(Solution, [1, 2, 3, 4, 5])
