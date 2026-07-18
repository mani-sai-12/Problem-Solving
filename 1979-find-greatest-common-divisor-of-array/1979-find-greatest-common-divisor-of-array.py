class Solution:
    def findGCD(self, nums: List[int]) -> int:
        max_gcd=0
        mn=min(nums)
        mx=max(nums)
        for i in range(1,mn+1):
            if mn%i==0 and mx%i==0:
                max_gcd=max(max_gcd,i)
        return max_gcd
