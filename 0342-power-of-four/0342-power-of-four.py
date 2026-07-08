class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        for x in range(31):
            if n==pow(4,x):
                return True
        return False
            