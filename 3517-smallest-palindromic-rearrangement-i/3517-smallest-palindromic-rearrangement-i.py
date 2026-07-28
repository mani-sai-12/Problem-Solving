class Solution:
    def smallestPalindrome(self, s: str) -> str:
        visited=[]
        first=''
        middle=''
        last=''
        a=sorted(s)
        arr=Counter(s)
        for ch in a:
            if ch in visited:
                continue
            c=arr[ch]
            if c%2==1:
                first+=((c//2)*ch)
                middle+=ch
            elif c%2==0:
                first+=((c//2)*ch)
            visited.append(ch)
        return first+middle+first[::-1]
        