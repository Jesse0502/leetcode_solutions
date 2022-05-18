class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        sl = sorted(stones)
        while len(sl) >= 2:
            y = sl.pop()
            x = sl.pop()
            if y > x:
                sl = sorted([*sl, y - x])
        return sl.pop() if len(sl) else 0


Solution.lastStoneWeight(Solution, [3, 7, 2])
