class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n=len(nums)
        nums.sort()
        for i in range(n-1):
            j=i+1
            if nums[i]==nums[j]:
                return True
        return False
        # d={}
        # for num in nums:
        #     if num not in d:
        #         d[num]=1
        #     else:
        #         d[num]+=1
        # for key,value in d.items():
        #     if value>=2:
        #         return True
        # return False
        