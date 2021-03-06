from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for n in nums:
            if hashmap.get(n, None):
                hashmap[n] += 1
            else:
                hashmap[n] = 1
        output = []
        for idx, (key, val) in enumerate(list(reversed(({k: v for k, v in sorted(hashmap.items(), key=lambda item: item[1])}.items())))):
            print(key, val)
            if idx < k:
                output.append(key)
        return output


Solution.topKFrequent(Solution, [4, 1, -1, 2, -1, 2, 3], 2)
