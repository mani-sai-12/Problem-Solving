class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        Sum=0
        for i in range(len(nums)):
            start=max(0,i-nums[i])
            Sum+=sum(nums[start:i+1])
        return Sum
        