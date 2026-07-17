class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        arr=list(map(str,s.split(" ")))
        for i in range(len(arr)-1,-1,-1):
            if arr[i]!="":
                return len(arr[i])
                break
        