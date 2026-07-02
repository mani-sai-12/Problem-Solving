class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        Sum=0
        for i in range(1,n+1):
            if i%m!=0:
                Sum+=i
            elif i%m==0:
                Sum-=i
        return Sum