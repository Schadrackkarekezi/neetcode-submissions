class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    
        strs = sorted(strs)
        anagrams = {}
        arr = []
        for i, word in enumerate(strs):
            anagrams[word] = i
        for i, word in strs:
            if word not in anagrams:
                arr.append([word]) 
        return arr
        




