from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lookup = {}

        for s in strs:
            sortedS = "".join(sorted(s))

            if sortedS not in lookup:
                lookup[sortedS] = [s]
            else:
                lookup[sortedS].append(s)

        return lookup.values()
