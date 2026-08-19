class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap ={}
        for i, j in enumerate(nums):
            dif = target - j
            if dif in hashmap:
                return[hashmap[dif], i]
            hashmap[j] = i
        return []




                
        