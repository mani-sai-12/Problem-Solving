class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        S_Counter={}
        T_Counter={}
        for i in range(len(s)):
            if s[i] not in S_Counter:
                S_Counter[s[i]]=i
            if t[i] not in T_Counter:
                T_Counter[t[i]]=i
            if S_Counter[s[i]]!=T_Counter[t[i]]:
                return False
        return True
        