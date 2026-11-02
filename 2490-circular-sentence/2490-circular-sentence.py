class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        arr=list(map(str,sentence.split()))
        for i in range(len(arr)):
            if i==len(arr)-1:
                if arr[i][-1]!=arr[0][0]:
                    return False
            elif arr[i][-1]!=arr[i+1][0]:
                return False
        return True

        