class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        ans=[]
        Min=min(nums)
        Max=max(nums)
        for i in range(Min,Max):
            if i not in nums:
                ans.append(i)
        return ans