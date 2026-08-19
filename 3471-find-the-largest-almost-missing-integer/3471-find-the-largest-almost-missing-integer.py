class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        d={}
        Max=-1
        i=0
        j=k-1
        while j<len(nums):
            a=nums[i:j+1]
            for num in set(a):
                d[num]=d.get(num,0)+1
            i+=1
            j+=1
        for num in d:
            if d[num]==1:
                Max=max(Max,num)
        return Max
        