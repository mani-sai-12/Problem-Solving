class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans=[]
        for i in range(0,n):
            j=i+1
            if j%3==0 and j%5==0:
                ans.append("FizzBuzz")
                continue
            elif j%3==0:
                ans.append("Fizz")
                continue
            elif j%5==0:
                ans.append("Buzz")
                continue
            else:
                ans.append(str(i+1))
        return ans
            
        