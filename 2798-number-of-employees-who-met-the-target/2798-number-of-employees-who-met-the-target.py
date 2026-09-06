class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        n=len(hours)
        c=0
        if max(hours)<target:
            return 0
        for i in range(n):
            if hours[i]>=target:
                c+=1
        return c