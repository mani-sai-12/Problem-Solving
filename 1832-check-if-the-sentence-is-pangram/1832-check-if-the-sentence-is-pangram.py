class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        A=Counter(sentence)
        return (True if len(A)==26 else False)