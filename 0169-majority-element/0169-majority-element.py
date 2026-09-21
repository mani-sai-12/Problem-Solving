class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        a=Counter(nums)
        res=max(a,key=a.get)
        return res
        