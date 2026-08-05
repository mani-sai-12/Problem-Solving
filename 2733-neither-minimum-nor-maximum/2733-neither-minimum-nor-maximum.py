class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums)<=2:
            return -1
        nums.sort()
        Min=min(nums)
        return nums[nums.index(Min)+1]