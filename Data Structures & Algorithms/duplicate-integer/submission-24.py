class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        mums = sorted(nums)
        for i in range(1,len(mums)):
            if  mums[i-1] == mums[i]:
                return True
        return False


   
