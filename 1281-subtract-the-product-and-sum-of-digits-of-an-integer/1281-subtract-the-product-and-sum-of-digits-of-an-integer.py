class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        Sum,Product =0,1
        while(n!=0):
            last_digit=n%10
            Sum+=last_digit
            Product*=last_digit
            n=n//10
        return Product-Sum

        