
class Solution:
    def frequencySort(self, s: str) -> str:
        d=Counter(s)
        ans=''
        sorted_d=sorted(d,key=d.get,reverse=True)
        for key in sorted_d:
            ans+=key*d[key]
        return ans
