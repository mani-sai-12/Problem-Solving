from collections import deque
class Solution:
    def maxDepth(self, s: str) -> int:
        MaxL=0
        # brackets=['(',')']
        stack=deque()
        for i in range(len(s)):
            if s[i] =='(':
                stack.append(s[i])
            elif s[i]==')':
                MaxL=max(MaxL,len(stack))
                stack.pop()
        return MaxL
