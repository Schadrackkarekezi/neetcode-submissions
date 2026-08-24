class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        mums = sorted(nums)
        for i in range(len(mums)):
            if  nums[i] == nums[i+1]:
                return True
        
        return False


   
