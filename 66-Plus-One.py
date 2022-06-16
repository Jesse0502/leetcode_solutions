from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        inc = ""
        for d in digits:
            inc += str(d)
        inc = int(inc) + 1
        output = []
        for i in str(inc):
            output.append(int(i))
        return output


Solution.plusOne(Solution, [10, 1, 2, 3, 4])
