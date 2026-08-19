class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        has = {}
        for i, j in enumerate(nums):
            has[j] = i
        for s in has:
            dif = target - s
            if dif in has:
                return[has[dif], s]
        return []





                
        