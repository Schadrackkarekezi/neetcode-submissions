class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        mums = sorted(nums)
        for i in range(len(mums)):
            if  nums[i-1] == nums[i]:
                return True
        return False


   
