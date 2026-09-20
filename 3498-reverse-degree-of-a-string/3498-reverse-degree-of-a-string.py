class Solution:
    def reverseDegree(self, s: str) -> int:
        A="zyxwvutsrqponmlkjihgfedcba"
        Sum,k,i=0,1,0
        while(i<len(s)):
            Sum+=(A.index(s[i])+1)*k
            i+=1
            k+=1
        return Sum


        