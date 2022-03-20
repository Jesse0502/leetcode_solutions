from pprint import pprint


class Solution:
    def romanToInt(self, s: str) -> int:
        arr = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        res = arr[s[0]]
        last = arr[s[0]]
        for idx, curr in enumerate(s):
            if idx > 0:
                if last < arr[curr]:
                    res += arr[curr] - 2*last
                else:
                    res += arr[curr]
            last = arr[curr]
        return res


print("sol", Solution.romanToInt("", "LVIII"))
