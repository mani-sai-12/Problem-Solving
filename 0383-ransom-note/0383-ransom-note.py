class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        c_r=Counter(ransomNote)
        c_m=Counter(magazine)
        for ch in ransomNote:
            if c_m[ch]<=0:
                return False
            c_m[ch]-=1
        return True
        