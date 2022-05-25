class Solution:
    def hammingWeight(self, n: int) -> int:
        stripZeros = str(bin(n)).lstrip("0")
        output = 0
        for s in stripZeros:
            if s == "1":
                output += 1
        return output


Solution.hammingWeight(Solution, bin(11))
