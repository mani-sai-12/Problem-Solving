class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        a=set(nums)
        if len(nums)==len(a):
            return False
        return True
        # a=Counter(nums)
        # first=a.most_common(1)[0]
        # if first[1]>=2:
        #     return True
        # else:
        #     return False
        