class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(s)
        t = sorted(t)
        countS , countT = {}, {}
        if t != s :
            return False
        for i in range(len(s)):
            if s[i] != t[1]:
                return False
        
