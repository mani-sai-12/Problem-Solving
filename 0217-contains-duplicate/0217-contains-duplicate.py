class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                return True
        return False
        # a=Counter(nums)
        # first=a.most_common(1)[0]
        # if first[1]>=2:
        #     return True
        # else:
        #     return False
        