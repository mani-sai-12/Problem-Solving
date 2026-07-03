class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res=[]
        Sum=0
        for i in range(len(nums)):
            if i==0:
                res.append(nums[i])
                Sum+=nums[i]
            else:
                Sum+=nums[i]
                res.append(Sum)
        return res
        