class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        # a=sorted(nums)
        # if nums==a or nums==a[::-1]:
        #     return True
        # else:
        #     return False
        return nums==sorted(nums) or nums==sorted(nums, reverse=True)
        