class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        Max=0
        n=len(sentences)
        for i in range(n):
            Max=max(Max,len(sentences[i].split(" ")))
        return Max
        