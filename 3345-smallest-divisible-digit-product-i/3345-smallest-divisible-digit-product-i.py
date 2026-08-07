class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        end=True
        while (end):
            a=list(map(int,str(n)))
            if prod(a)%t==0:
                return n
            n+=1
        