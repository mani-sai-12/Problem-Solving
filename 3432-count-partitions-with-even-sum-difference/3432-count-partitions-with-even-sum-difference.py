class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        count=0
        n=len(nums)
        for i in range(n-1):
            a=sum(nums[:i+1])
            b=sum(nums[i+1:n])
            Sum=a-b
            if Sum%2!=0 and Sum==0:
                continue
            elif Sum%2==0:
                count+=1
            
        return count