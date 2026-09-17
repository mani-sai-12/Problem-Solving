class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        a=[]
        for i in range(len(nums)):
            a.append(nums[i]**2)
        a.sort()
        return a