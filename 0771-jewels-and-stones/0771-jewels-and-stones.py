class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        Sum=0
        d=Counter(stones)
        for jewel in jewels:
            if jewel in d:
                Sum+=d[jewel]
        return Sum
        