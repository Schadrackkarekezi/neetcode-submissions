class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(s)
        t = sorted(t)

        for i in range(len(s)):
            for t in range(len(t)):
                if s[i] != t[t]:
                    return False
        return True
