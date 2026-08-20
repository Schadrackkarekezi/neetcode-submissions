class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False
        
        s = sorted(s)
        t = sorted(s)

        for i in s:
            for j in t:
                if j != i :
                    return False
        return True


        