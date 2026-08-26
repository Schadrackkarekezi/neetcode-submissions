class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ss = sorted(s)
        st = sorted(t)
        if len(s) == len(t):
            return False
        for i in ss:
            for j in st:
                if i != j:
                    return False
        return True




            
            


        