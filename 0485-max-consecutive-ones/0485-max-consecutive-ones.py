class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans=[]
        count=0
        for i in range(len(nums)):
            if nums[i]!=1:
                ans.append(count)
                count=0
                continue
            elif i<=len(nums)-1:
                count+=1
                ans.append(count)
                continue
            else:
                count+=1
        return max(ans)
        