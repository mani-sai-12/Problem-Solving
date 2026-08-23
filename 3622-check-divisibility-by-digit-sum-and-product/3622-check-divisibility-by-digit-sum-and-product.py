class Solution:
    def checkDivisibility(self, n: int) -> bool:
        Sum=0
        Prod=1
        original_num=n
        while n>0:
            digit=n%10
            Sum+=digit
            Prod*=digit
            n//=10
        if original_num%(Sum+Prod)==0:
            return True
        else:
            return False
    
        