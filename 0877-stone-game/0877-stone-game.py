class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        arr=piles
        a,b=0,0
        for i in range(len(piles)):
            if i%2==0:
                a+=max(arr)
                arr.remove(max(arr))
            else:
                b+=max(arr)
                arr.remove(max(arr))
        if a>b:
            return True
        else:
            return False