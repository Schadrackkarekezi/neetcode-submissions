class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hasmap = {}
        for i, j in enumerate(nums):
            diff = target - j
            if diff in hasmap and hasmap[diff] !=i:
                    return [hasmap[diff], i]
            hasmap[j] = i
        return []




                
        