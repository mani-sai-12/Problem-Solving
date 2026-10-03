class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_set=set()
        MaxL=0
        i=0
        for j in range(0,len(s)):
            while s[j] in hash_set:
                hash_set.remove(s[i])
                i+=1
            hash_set.add(s[j])
            MaxL=max(MaxL,j-i+1)
            j+=1
        return MaxL