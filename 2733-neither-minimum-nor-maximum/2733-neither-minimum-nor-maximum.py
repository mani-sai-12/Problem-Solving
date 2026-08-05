class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        # nums.sort()
        # Min=min(nums)
        # return nums[nums.index(Min)+1]
        for i in range(len(nums)):
            if nums[i]!=min(nums) and nums[i]!=max(nums):
                return nums[i]
        return -1