class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums = sorted(nums)

        for i in range(1, len(nums)):
            nums[i-1] = nums[i]
            return True

        return False
