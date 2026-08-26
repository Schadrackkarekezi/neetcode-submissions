class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}
        return Counter(s) == Counter(t)



            
            


        