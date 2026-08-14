class Solution:
    def sortColors(self, nums: List[int]) -> None:
        c_0,c_1,c_2=0,0,0
        for x in nums:
            if x==0:
                c_0+=1
            elif x==1:
                c_1+=1
            elif x==2:
                c_2+=1
        for i in range(0,c_0):
            nums[i]=0
        for i in range(c_0,c_0+c_1):
            nums[i]=1
        for i in range(c_0+c_1,len(nums)):
            nums[i]=2

        
            
        
