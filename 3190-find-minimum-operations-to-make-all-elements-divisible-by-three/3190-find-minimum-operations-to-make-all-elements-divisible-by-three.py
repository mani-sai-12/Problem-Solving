class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        op_count=0
        for num in nums:
            if num%3!=0:
                op_count+=1
        return op_count

        