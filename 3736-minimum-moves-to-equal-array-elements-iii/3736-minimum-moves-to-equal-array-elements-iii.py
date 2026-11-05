class Solution:
    def minMoves(self, nums: List[int]) -> int:
        Max=max(nums)
        moves=0
        for i in range(len(nums)):
            moves+=Max-nums[i]
        return moves
        