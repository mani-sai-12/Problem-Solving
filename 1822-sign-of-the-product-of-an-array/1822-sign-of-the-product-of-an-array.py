class Solution:
    def arraySign(self, nums: list[int]) -> int:
        a=prod(nums)
        if a>0:
            return 1
        elif a<0:
            return -1
        else:
            return 0