from itertools import permutations
class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        # perms=[int(''.join(map(str,p))) for p in permutations(digits,r=3)
        # if int(''.join(map(str, p))) % 2 == 0]
        even_num=[]
        for p in permutations(digits,r=3):
            if p[0]!=0:
                num=int(''.join(map(str,p)))
                if num%2==0:
                    even_num.append(num)
        
        return len(set(even_num))
        