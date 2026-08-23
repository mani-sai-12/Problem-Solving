class Solution:
    def checkDivisibility(self, n: int) -> bool:
        S,P,Num=0,1,n
        while n>0:
            digit=n%10
            S+=digit
            P*=digit
            n//=10
        if Num%(S+P)!=0:
            return False
        return True
    
        