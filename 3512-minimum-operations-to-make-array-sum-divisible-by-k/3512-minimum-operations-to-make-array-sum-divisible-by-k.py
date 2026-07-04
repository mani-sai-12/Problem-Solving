class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        Sum=sum(nums)
        if Sum%k==0:
            return 0
        if Sum<k:
            return Sum
        if Sum%k!=0:
            return Sum%k
        