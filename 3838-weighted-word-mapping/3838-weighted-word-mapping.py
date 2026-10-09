class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        res=''
        for i in range(len(words)):
            Sum=0
            for ch in words[i]:
                Sum+=weights[ord(ch)-ord('a')]
            mod=Sum%26
            res+=chr(ord('z')-mod)
        return res

