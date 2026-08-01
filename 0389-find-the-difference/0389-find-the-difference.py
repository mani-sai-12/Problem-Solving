class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        arr=Counter(s)
        ans=''
        for ch in t:
            if ch not in s or arr[ch]==0:
                ans+=ch
            arr[ch]-=1
        return ans