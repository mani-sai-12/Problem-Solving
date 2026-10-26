class Solution:
    def addBinary(self, a: str, b: str) -> str:
        Sum=str(bin(int(a,2)+int(b,2)))
        return Sum[2:]
        