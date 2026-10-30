class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        res=[]
        arr=[]*len(nums)
        arr[:]=nums[:]
        arr.sort()
        for num in nums:
            index=arr.index(num)
            res.append(index)
        return res

        