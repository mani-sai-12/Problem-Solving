class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res=[nums[0]]
        # Sum=res[0]
        i=0
        while i<len(nums)-1:
            res.append(nums[i+1]+res[i])
            i+=1
        # for i in range(len(nums)):
        #     if i==0:
        #         res.append(nums[i])
        #         Sum+=nums[i]
        #     else:
        #         Sum+=nums[i]
        #         res.append(Sum)
        return res
        