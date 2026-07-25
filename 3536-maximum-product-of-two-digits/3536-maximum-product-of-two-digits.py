class Solution:
    def maxProduct(self, n: int) -> int:
        Max=0
        S=str(n)
        for i in range(len(S)-1):
            for j in range(i+1,len(S)):
                Max=max(Max,(int(S[i])*int(S[j])))
        return Max
        