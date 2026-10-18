class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        res=[]
        d=Counter(nums)
        for num in set(nums):
            if d[num]>=2:
                res.append(num)
        return res
