from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []
        for num in range(n + 1):
            getbin = str(bin(int(num)))[2:]
            sumBits = 0
            for nu in getbin:
                sumBits += int(nu)
            output.append(sumBits)
        return output


Solution.countBits(Solution, 27)
