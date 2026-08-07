class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans=[]
        a=set(nums)
        for i in range(0,len(nums)):
            if i+1 not in a:
                ans.append(i+1)
        return ans

        