class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = {}
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            counts[s[i]] = 1 + counts.get(s[i], 0)
        
        for i in range(len(t)):
            if t[i] not in counts or counts[i] == 0:
                return False
        return True

        