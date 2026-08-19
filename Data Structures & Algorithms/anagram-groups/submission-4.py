class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    
        strs = sorted(strs)
        anagrams = {}
        arr = []
        for i, word in enumerate(strs):
            anagrams[word] = i
        for word in strs:
            if word in anagrams:
                index = anagrams[word]
                arr[index].append(word)   
        return arr
        




