class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        d={}
        for ch in sentence:
            if ch in d:
                d[ch]+=1
            else:
                d[ch]=1
        return (True if len(d)==26 else False)