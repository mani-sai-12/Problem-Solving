class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        end=True
        while (end):
            s=str(n)
            a=list(map(int,s))
            if prod(a)%t==0:
                return n
            n+=1
        