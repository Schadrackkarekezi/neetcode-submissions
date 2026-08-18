class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(s)
        t = sorted(t)
        if t != s :
            return False
        for i in range(len(s)):
            for j in range(len(t)):
                if s[i] != t[j]:
                    return False
        return True
