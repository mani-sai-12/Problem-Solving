class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        d=Counter(nums)
        for num in set(nums):
            if d[num]==1:
                return num
        