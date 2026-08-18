class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS , countT = {}, {}
        if t != s :
            return False
        for i in range(len(s)):
            countS[s[i]]= 1 + countS.get(s[i],0)
            countT[t[i]] = 1 + countT.get([i],0)
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False

            