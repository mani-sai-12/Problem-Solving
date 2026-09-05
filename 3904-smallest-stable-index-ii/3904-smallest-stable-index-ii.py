class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n=len(nums)
        preff=[0]*n
        suff=[0]*n
        preff[0]=nums[0]
        for i in range(1,n):
            preff[i]=max(preff[i-1],nums[i])
        
        suff[n-1]=nums[n-1]
        for i in range(n-2,-1,-1):
            suff[i]=min(suff[i+1],nums[i])
        for i in range(n):
            if preff[i]-suff[i]<=k:
                return i
        return -1