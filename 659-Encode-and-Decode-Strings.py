class Solution:

    def encode(self, strs):
        output = ""
        for s in strs:
            prefix = str(len(s)) + "#"
            output += prefix + s
        return output

    def decode(self, str):
        res, i = [], 0
        while i < len(str):
            j = i
            while str[j] != "#":
                j += 1
            length = int(str[i:j])
            res.append(str[j+1:j+1+length])
            i = j + 1 + length
        return res


Solution.decode(
    Solution.encode(Solution, ['hello', "world"])
)
