class Solution:
    def isHappy(self, n: int) -> bool:
        if n < 0:
            return False
        replace_int = n
        arr = []
        while replace_int != 1:

            newI: int = 0
            for num in str(replace_int):
                newI += int(num) * int(num)
            if newI in arr:
                return False
            arr.append(replace_int)
            replace_int = newI

        return True


Solution.isHappy(Solution, 2)
