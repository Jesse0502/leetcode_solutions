class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        output = True
        rdMag = []
        for w in magazine:
            rdMag.append(w)
        
        for s in ransomNote:
            if s in rdMag:
                rdMag.remove(s)
            else:
                output = False
        return output

print(Solution.canConstruct("", "aa", "aab"))