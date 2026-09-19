class Solution:
    def threeConsecutiveOdds(self, arr: list[int]) -> bool:
        c=0
        for num in arr:
            if num%2==0:
                c=0
            elif num%2==1:
                c+=1
            if c==3:
                return True
        return False
        