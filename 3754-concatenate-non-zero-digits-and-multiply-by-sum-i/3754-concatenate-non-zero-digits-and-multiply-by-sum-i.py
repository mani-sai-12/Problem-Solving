class Solution:
    def sumAndMultiply(self, n: int) -> int:
        s=str(n)
        x=""
        Sum=0
        for ch in s :
            if ch!='0':
                x+=ch
                Sum+=int(ch)
        if x=="":
            return 0
        else:
            return int(x)*Sum