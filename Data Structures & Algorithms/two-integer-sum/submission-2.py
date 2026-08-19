class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        has = {}

        for i, j in enumerate(nums):
            has[i] = j

        for s in range(1,len(has)):
            if has[s-1] + has[s] == target:
                return[s-1, s]
        return []





                
        