class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        j=0
        for i in range(len(nums1)):
            if i>=m:
                nums1[i],nums2[j]=nums2[j],nums1[i]
                j+=1
        return nums1.sort()
        