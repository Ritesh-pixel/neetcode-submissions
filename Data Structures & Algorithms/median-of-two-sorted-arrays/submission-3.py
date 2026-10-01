class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1=nums1+nums2
        n1=sorted(n1)
        n2=len(n1)
        if n2%2==0:
            m1,m2=(n2//2),(n2//2)-1
            return float(n1[m1]+n1[m2])/2
        else:
            m=n2//2
            return n1[m]
        return -1