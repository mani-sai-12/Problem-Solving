class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        ans=[-1]*len(nums1)
        for i in range(len(nums1)):
            for j in range(nums2.index(nums1[i]),len(nums2)):
                if nums2[j]>nums1[i]:
                    ans[i]=nums2[j]
                    break
        return ans