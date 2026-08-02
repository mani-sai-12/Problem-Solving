class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        a=sorted(nums)
        b=sorted(nums,reverse=True)
        # if nums==a or nums==a[::-1]:
        #     return True
        # else:
        #     return False
        return nums==a or nums==b
        