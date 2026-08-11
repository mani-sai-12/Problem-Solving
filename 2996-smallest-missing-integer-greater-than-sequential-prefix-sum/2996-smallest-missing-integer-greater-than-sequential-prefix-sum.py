class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        a=[]
        a[::]=nums[::]
        a.sort()
        Sum=nums[0]
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]+1:
                break
            Sum+=nums[i]
        while(True):
            if Sum not in nums:
                break
            Sum+=1
        return Sum