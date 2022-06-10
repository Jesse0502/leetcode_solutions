"""
find the index where needle start if it's in the haystack

loop through the haystack and check if the curr index matches with needle[0]
if curr == needle[0] then check if heystack[curr: curr + len(needle)] == needle
if true return curr
else return -1
"""


class Solution():
    def strStr(self, haystack, needle):
        for idx, i in enumerate(haystack):
            if(haystack[idx] == needle[0]):
                if(haystack[idx: idx + len(needle)] == needle):
                    return idx
        return -1


Solution.strStr(Solution, "hello", "ll")
