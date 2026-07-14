class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        a=Counter(nums)
        first=a.most_common(1)[0]
        if first[1]>=2:
            return True
        else:
            return False
        