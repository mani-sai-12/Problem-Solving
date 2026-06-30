class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        Sum=0
        while(n!=0):
            last_digit=n%10
            Sum+=last_digit
            n=n//10
        return Sum

        