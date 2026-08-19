class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    
        strs = sorted(strs)
        anagrams = {}
        arr = []
        for i, word in enumerate(strs):
            anagrams[word] = i
        for i, word in enumerate(strs):
            if word in anagrams:
                arr[i].append(word)   
        return arr
        




