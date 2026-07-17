class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i,j=0,0
        sl,tl=len(s),len(t)
        while(i<sl and j<tl):
            if s[i]==t[j]:
                j+=1
            i+=1
        return tl-j
        