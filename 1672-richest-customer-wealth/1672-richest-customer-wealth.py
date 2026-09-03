class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        Max=0
        for i in range(len(accounts)):
            Sum=sum(accounts[i])
            Max=max(Max,Sum)
        return Max
        