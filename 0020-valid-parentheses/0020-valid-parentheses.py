from collections import deque
class Solution:
    def isValid(self, s: str) -> bool: 
        if len(s)==1:
            return False
        d={
            ')':'(',
            ']':'[',
            '}':'{'
        }
        stack=deque()
        for ch in s:
            if ch in '([{':
                stack.append(ch)
            
            elif len(stack)!=0 and d[ch]==stack[-1]:
                stack.pop()
            else:
                stack.append(ch)
        return (True if len(stack)==0 else False)
    

        