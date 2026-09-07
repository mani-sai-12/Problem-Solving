class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n=len(nums)
        SumL=[0]*n
        SumR=[0]*n
        SumL[0]=nums[0]
        for i in range(1,n):
            SumL[i]=SumL[i-1]+nums[i]
        
        SumR[n-1]=nums[n-1]
        for i in range(n-2,-1,-1):
            SumR[i]=SumR[i+1]+nums[i]
        
        for i in range(n):
            if SumL[i]==SumR[i]:
                return i
        return -1

        