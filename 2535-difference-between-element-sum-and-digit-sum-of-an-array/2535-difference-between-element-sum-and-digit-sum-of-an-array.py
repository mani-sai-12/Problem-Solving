class Solution:
    def digitSum(self,n):
        ds=0
        while(n!=0):
            digit=n%10
            ds+=digit
            n=n//10
        return ds



    def differenceOfSum(self, nums: List[int]) -> int:
        Sum=0
        if max(nums)<=9:
            return 0
        for i in range(len(nums)):
            if nums[i]<=9:
                Sum+=nums[i]
            else:
                Sum+=self.digitSum(nums[i])
        return sum(nums)-Sum

