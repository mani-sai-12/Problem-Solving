class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        p_c,n_c=0,0
        for i in range(len(nums)):
            if nums[i]>0:
                p_c+=1
            elif nums[i]<0:
                n_c+=1
        return max(p_c,n_c)