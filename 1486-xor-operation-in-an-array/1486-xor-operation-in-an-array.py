class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums=[0]
        for i in range(n):
            num=(start+2*i)
            nums.append(nums[i]^num)
        return nums[-1]

