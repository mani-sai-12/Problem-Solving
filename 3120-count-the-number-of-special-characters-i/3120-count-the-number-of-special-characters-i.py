class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        c=0
        if word.islower() or word.isupper():
            return 0
        l=''
        u=''
        for ch in word:
            if ch.islower():
                l+=ch
            else:
                u+=ch
        for ch in l:
            if ch.upper() in u:
                c+=1
                u=u.replace(ch.upper(),'')
        return c



        