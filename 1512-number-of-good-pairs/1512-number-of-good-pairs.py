class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        visited=[]
        count=0
        a=Counter(nums)
        for i in range(len(nums)):
            if nums[i] in visited:
                continue
            n=a[nums[i]]
            count+=(n*(n-1)//2)
            visited.append(nums[i])
        return count
        
