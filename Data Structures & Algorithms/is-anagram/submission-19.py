class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = {}
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            counts[s[i]] = 1 + counts.get(s[i], 0)
        
        for j in range(len(t)):
            if t[j] not in counts or counts[t[j]] == 0:
                return False
            counts[t[j]] -=1
                
        return True

        