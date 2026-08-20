class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counterT, counterS = {},{}
        if len(t) != len(s):
            return False
        for i in s:
            counterS[s[i]] = 1 + counterT.get(s[i], 0)
            counterS[t[i]] = 1 + counterT.get(t[i], 0)

        return counterS == counterT 



            
            


        