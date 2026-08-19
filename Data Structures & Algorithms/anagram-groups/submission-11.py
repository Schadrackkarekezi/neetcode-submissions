class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    
        strss = sorted(strs)
        anagrams = {}
        arr = []
        for i, word in enumerate(strss):
            anagrams[word] = i
        for word in strss:
            if word not in anagrams:
                arr.append([word]) 
            
        return arr
        




