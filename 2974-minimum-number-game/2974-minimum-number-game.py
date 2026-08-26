class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        res=[]
        n=len(nums)
        while nums:
            a=min(nums)
            nums.remove(a)
            b=min(nums)
            nums.remove(b)
            res.append(b)
            res.append(a)
            
        return res


        