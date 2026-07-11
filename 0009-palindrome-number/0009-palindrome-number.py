class Solution:
    def isPalindrome(self, x: int) -> bool:
        a=x
        rev=0
        while(a>0):
            digit=a%10
            rev=rev*10+digit
            a=a//10
        if x==rev:
            return True
        return False