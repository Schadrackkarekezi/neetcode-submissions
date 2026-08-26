class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cs ={}
        ct = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            cs[s[i]] = 1 + cs.get(cs[i],0)
            ct[t[i]] = 1 + ct.get(ct[i], 0)
        return cs == ct


   



            
            


        